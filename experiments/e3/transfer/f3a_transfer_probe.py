#!/usr/bin/env python3
"""F3 A transfer probe (RESEARCH ONLY). Offline, no LLM, no network.

Question: after a pause, does a successor reading what a system stored still see
(1) the results, (2) that the work is DONE, and (3) that production integration
(routing) was NOT part of the request?

Usage: python3 -B f3a_transfer_probe.py --target titan|crystal --repo <clean copy> --out <json>
Run each target in its own process (both repos have a package called `core`).
The repo given must be a COPY; this script writes only into a temp dir.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile

OWNER = ("Прогони через «Меридиан» пробный пакет адресов из октябрьской выгрузки и скажи, как он справился: "
         "сколько адресов распознал и какая задержка. Мне это нужно только для отчёта, маршрутизацию менять не будем.")
RESULTS = ("Пробный пакет из 50 адресов октябрьской выгрузки: распознано 48, у 2 низкая точность (улица без дома), "
           "средняя задержка 180 мс на адрес.")
STATE = ("Штатный вызов «Меридиана» в routing не подключён, обработка адресов с низкой точностью не реализована, "
         "платный тариф не оформлен.")
DONE = "Работа по просьбе завершена: отчёт с цифрами готов и отправлен владельцу."
SCOPE_EXCL = "Вне договорённости (владелец не просил): подключение «Меридиана» в routing, обработка низкой точности, платный тариф."

# keyword-based information units (exploratory; documented as such in the report)
IU = {
    "result": lambda t: "48" in t and "180" in t,
    "done": lambda t: bool(re.search(r"работа по просьбе завершена|отчёт[^.]{0,30}готов|просьба выполнена|выполнено", t, re.I)),
    "scope_excludes_routing": lambda t: bool(re.search(
        r"маршрутизаци\w*\s+менять\s+не\s+будем|не\s+будем\s+менять\s+маршрутизаци|вне договорённости|владелец не просил"
        r"|не\s+входил\w*\s+в\s+(просьбу|договорённость)|только для отчёта", t, re.I)),
}


def evaluate(slots: dict[str, str]) -> dict:
    corpus = "\n".join(slots.values())
    found = {k: f(corpus) for k, f in IU.items()}
    where = {k: [s for s, v in slots.items() if f(v)] for k, f in IU.items()}
    return {"found": found, "where": where,
            "SUCCESS": all(found.values())}


def run_titan(repo: str) -> dict:
    sys.path.insert(0, repo)
    from core.conversation_consolidation import ConversationConsolidator
    from core.continuity import ConversationBridge
    from core.goal_stack import GoalStack
    out = {}
    tmp = tempfile.mkdtemp()

    def notebook_case(name, goal, insights, conclusion):
        db = os.path.join(tmp, f"{name}.db")
        c = ConversationConsolidator(db)
        for i in insights:
            c.add_insight(chat_id=name, insight=i)
        c.finalize(chat_id=name, main_topic="Меридиан для склада", user_goal=goal, conclusion=conclusion, facts_count=2)
        # "pause": a fresh consolidator on the same file, as a successor would open it
        c2 = ConversationConsolidator(db)
        nb = c2.get_notebook(name)
        ep = ConversationBridge(c2).get_episode(name)
        nb_slots = {"user_goal": nb.user_goal, "conclusion": nb.conclusion, "key_insights": "\n".join(nb.key_insights)}
        ep_slots = {"user_goal": ep.user_goal, "conclusion": ep.conclusion, "key_insights": "\n".join(ep.key_insights)}
        return {"notebook": evaluate(nb_slots), "episode": evaluate(ep_slots), "stored_slots": nb_slots,
                "lossless_notebook_to_episode": nb_slots == {k: v for k, v in ep_slots.items()}
                or all(" ".join(nb_slots[k].split()) == ep_slots[k] for k in nb_slots)}

    out["T1_full_in_designed_slots"] = notebook_case("t1", OWNER, [RESULTS, STATE], f"{DONE} {SCOPE_EXCL}")
    out["T2_typical_short_summary"] = notebook_case("t2", "Проверка «Меридиана» на пробном пакете адресов", [RESULTS],
                                                    "Пробный прогон выполнен: 48 из 50 распознаны, задержка 180 мс.")
    out["T2b_done_but_no_boundary"] = notebook_case("t2b", "Проверка «Меридиана» на пробном пакете адресов", [RESULTS],
                                                    "Работа по просьбе завершена: отчёт готов. 48 из 50 распознаны, задержка 180 мс.")
    out["T3_record_without_owner_words"] = notebook_case(
        "t3", "", [], f"Достигнуто: {RESULTS} Граница завершённой работы: только лабораторная проверка. {STATE} Маршрутизация не менялась.")

    # GoalStack: the only place with a status. Natural use: goal title = request, description = scope.
    gs = GoalStack(os.path.join(tmp, "goals.db"))
    g = gs.create(user_id="owner", title="Прогон пробного пакета через «Меридиан»", description=RESULTS)
    gs.update_status(g.goal_id, "done")
    g2 = GoalStack(os.path.join(tmp, "goals.db")).get(g.goal_id)
    out["T4_goalstack_typical"] = {"stored": {"title": g2.title, "description": g2.description, "status": g2.status},
                                   "eval": evaluate({"title": g2.title, "description": g2.description, "status": g2.status})}
    g3 = gs.create(user_id="owner", title=OWNER, description=f"{RESULTS} {SCOPE_EXCL}")
    gs.update_status(g3.goal_id, "done")
    g4 = GoalStack(os.path.join(tmp, "goals.db")).get(g3.goal_id)
    out["T5_goalstack_full"] = {"stored": {"title": g4.title[:80] + "…", "status": g4.status},
                                "eval": evaluate({"title": g4.title, "description": g4.description, "status": f"{DONE if g4.status == 'done' else ''}"})}
    out["T5_note"] = "status 'done' is a bare flag; for T5 its meaning ('работа завершена') is credited to the 'done' unit only because status==done"
    return out


def run_crystal(repo: str) -> dict:
    tmp = tempfile.mkdtemp()
    os.environ.update({"VELANTRIM_L3_BACKEND": "mock", "VELANTRIM_EMBEDDER": "hashing", "VELANTRIM_GENERATOR": "extractive",
                       "VELANTRIM_QUEUE_BACKEND": "sqlite", "VELANTRIM_DEMO_SEED": "1", "VELANTRIM_DB": os.path.join(tmp, "l1.db")})
    sys.path.insert(0, repo)
    from core import memory
    from core.ingest import ingest

    def fresh(name):
        memory.SQLITE_PATH = os.path.join(tmp, f"{name}.db")
        if hasattr(memory, "init_db"):
            try:
                memory.init_db()
            except Exception:
                pass

    def case(name, calls):
        fresh(name)
        log = []
        for text, kw in calls:
            r = ingest(text, **kw)
            log.append({"text": text[:60] + "…", "kw": {k: v for k, v in kw.items() if k != "metadata"},
                        "accepted": r.get("accepted"), "reason": r.get("reason")})
        facts = memory.get_all_facts()
        rows = []
        for f in facts:
            md = f.get("metadata")
            if isinstance(md, str):
                try:
                    md = json.loads(md or "{}")
                except Exception:
                    md = {}
            rows.append({"claim": f.get("claim"), "claim_type": f.get("claim_type"), "source_status": f.get("source_status"),
                         "epistemic_state": f.get("epistemic_state"), "source": f.get("source"), "metadata": md})
        slots = {f"claim[{i}:{r['claim_type']}/{r['source_status']}]": r["claim"] or "" for i, r in enumerate(rows)}
        return {"ingest_log": log, "restored": rows, "eval": evaluate(slots)}

    out = {}
    out["C1_naive_default_ingest"] = case("c1", [
        (OWNER, {"source": "user"}),
        (RESULTS, {"source": "executor"}),
        (DONE, {"source": "executor"}),
    ])
    out["C2_convention_typed_claims"] = case("c2", [
        (OWNER, {"source": "user", "claim_type": "GOAL", "source_status": "USER_REPORTED", "metadata": {"task": "F3A", "role": "owner_request"}}),
        (SCOPE_EXCL, {"source": "user", "claim_type": "PREFERENCE", "source_status": "USER_REPORTED", "metadata": {"task": "F3A", "role": "scope_exclusion"}}),
        (RESULTS, {"source": "executor", "source_status": "DERIVED", "metadata": {"task": "F3A", "role": "result"}}),
        (DONE, {"source": "executor", "source_status": "SYSTEM_AUTHORED", "metadata": {"task": "F3A", "role": "state"}}),
    ])
    out["C2b_done_but_no_boundary"] = case("c2b", [
        (RESULTS, {"source": "executor"}),
        (DONE, {"source": "executor"}),
    ])
    out["C3_record_without_owner_words"] = case("c3", [
        (f"Достигнуто: {RESULTS}", {"source": "executor"}),
        (f"Граница завершённой работы: только лабораторная проверка. {STATE} Маршрутизация не менялась.", {"source": "executor"}),
    ])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", choices=["titan", "crystal"], required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = run_titan(a.repo) if a.target == "titan" else run_crystal(a.repo)
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    for name, v in res.items():
        if isinstance(v, dict):
            ev = v.get("episode") or v.get("eval") or {}
            print(f"{name:36s} SUCCESS={ev.get('SUCCESS')} found={ev.get('found')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
