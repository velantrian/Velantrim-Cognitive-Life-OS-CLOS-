#!/usr/bin/env python3
"""Build the blind-annotation package (RESEARCH ONLY). Offline; no API calls.

Writes experiments/e3/annotation/REFERENCE.md from the frozen fixtures and copies
the blind sheet next to it. The reference deliberately contains NO expected action
labels, NO record texts, NO calibration summaries and NO variant names: the
annotator must not be able to infer which record variant produced an answer.

Included per episode: materials, the owner's words, the executor's answer to the
owner (what the owner was told), episode notes, and the ground truth about the
agreement. These are the facts against which claims about the past are checked.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "annotation"
RESULTS = HERE / "results" / "deepseek-pilot-45437512167"


def build_reference() -> str:
    fam = json.loads((HERE / "fixtures" / "families.json").read_text(encoding="utf-8"))
    frozen = json.loads((HERE / "frozen" / "episodes.json").read_text(encoding="utf-8"))
    told = {e["episode_id"]: e["decision"].get("public_answer", "") for e in frozen["episodes"]}
    cont = fam["continuations"]

    out = [
        "# Эталон для разметки (E3)",
        "",
        "Факты об эпизодах, с которыми сверяются утверждения о прошлом. Это **реальность**, а не чья-то запись.",
        "",
        "## Три реплики, на которые отвечал преемник (колонка `row`)",
        "",
        f"- `row1`: «{cont['row1']}»",
        f"- `row2`: «{cont['row2']}»",
        f"- `row3`: «{cont['row3']}»",
        "",
    ]
    for f in fam["families"]:
        for story in ("A", "B"):
            s = f["stories"][story]
            eid = f"{f['id']}{story}"
            out += [
                f"## {eid} · {f['title']}",
                "",
                "**Материалы по задаче (что известно о состоянии дел):**",
                "",
                *[("> " + line if line else ">") for line in f["materials"].split("\n")],
                "",
                f"**Слова владельца:** «{s['owner_request']}»",
                "",
                f"**Что исполнитель ответил владельцу:** «{told[eid]}»",
                "",
            ]
            if s.get("episode_notes"):
                out += [f"**Примечание к эпизоду:** {s['episode_notes']}.", ""]
            out += [f"**Истина о договорённости:** {s['truth']}", ""]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    OUT.mkdir(exist_ok=True)
    (OUT / "REFERENCE.md").write_text(build_reference(), encoding="utf-8")
    shutil.copyfile(RESULTS / "annotation_blind.csv", OUT / "annotation_blind.csv")
    print("written:", OUT / "REFERENCE.md", "and annotation_blind.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
