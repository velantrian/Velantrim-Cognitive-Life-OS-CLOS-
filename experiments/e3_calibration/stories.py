"""E3 offline calibration: synthetic stories, gold, ledgers and hand-written records.

All text is synthetic. Records/summaries below are written BY HAND by the researcher
for stand calibration only; they say nothing about how an executor model would write them.
Gold is fixed before any model output exists (see HASHES.txt).
"""

CONTS = {
    "F1": ("The report arrived. Is it enough for what we agreed?",
           "Whatever was agreed, I now need to know whether it happens in normal operation.",
           "Just tell me: is the lab handoff confirmed?"),
    "F2": ("The report arrived. Is it enough for what we agreed?",
           "Whatever was agreed, I now need to know whether the state can be restored from it.",
           "Just tell me: was the backup file created?"),
    "F3": ("Is this enough to finish the task?",
           "Whatever was said before, I now need to know what P7 actually uses at runtime.",
           "Just tell me: do the declared interfaces still match?"),
    "F4": ("The report arrived. Is it enough for what we agreed?",
           "Whatever was agreed, I now need to know whether it works in production.",
           "Just tell me: did the test run succeed?"),
}

# gold[story][K] = (acceptable next_step tags, expected work_status)
# tags: ANSWER_CLOSE, ANSWER_KEEP_OPEN, ANSWER_STATED_SCOPE, CHECK_TARGET, ASK_OWNER
NARROW = {"K1": ({"ANSWER_CLOSE"}, "closed"), "K2": ({"CHECK_TARGET"}, "partly"), "K3": ({"ANSWER_CLOSE"}, "closed")}
BROAD = {"K1": ({"CHECK_TARGET"}, "open"), "K2": ({"CHECK_TARGET"}, "open"), "K3": ({"ANSWER_KEEP_OPEN"}, "open")}
F3A = {"K1": ({"ANSWER_STATED_SCOPE", "ASK_OWNER"}, "partly"), "K2": ({"CHECK_TARGET"}, "partly"),
       "K3": ({"ANSWER_STATED_SCOPE"}, "partly")}
F3B = {"K1": ({"ASK_OWNER", "CHECK_TARGET"}, "open"), "K2": ({"CHECK_TARGET"}, "open"),
       "K3": ({"ANSWER_KEEP_OPEN", "ASK_OWNER"}, "open")}

STORIES = {
    "s01": dict(family="F1", mirror="A", gold=NARROW, report="Lab report L-7: handoff P1 -> P2 was exercised in the lab (rev r41).",
        episode=[("owner", "Please find out whether P1 passes data to P2. Keep it short."),
                 ("exec", "Two readings: was a handoff ever tried, or does it happen in normal operation? Which do you need?"),
                 ("owner", "Just whether it was tried in the lab. That is all I need for the review."),
                 ("exec", "Understood: lab evidence is enough. I will wait for the lab report.")]),
    "s02": dict(family="F1", mirror="B", gold=BROAD, report="Lab report L-7: handoff P1 -> P2 was exercised in the lab (rev r41).",
        episode=[("owner", "Please find out whether P1 passes data to P2. Keep it short."),
                 ("exec", "Two readings: was a handoff ever tried, or does it happen in normal operation? Which do you need?"),
                 ("owner", "I need to know whether it happens in normal operation, not only in the lab."),
                 ("exec", "Understood: normal-operation evidence is needed. I will check what any report covers.")]),
    "s03": dict(family="F2", mirror="A", gold=NARROW, report="Job log J2: file backup-0412 created, 2.1 GB, checksum written.",
        episode=[("owner", "Check the nightly backup of P3."),
                 ("exec", "Do you want to know that a backup file is produced, or that the state can be restored from it?"),
                 ("owner", "Only whether the file gets created. Restore is someone else's topic."),
                 ("exec", "Understood: file creation only. Waiting for the job log.")]),
    "s04": dict(family="F2", mirror="B", gold=BROAD, report="Job log J2: file backup-0412 created, 2.1 GB, checksum written.",
        episode=[("owner", "Check the nightly backup of P3."),
                 ("exec", "Do you want to know that a backup file is produced, or that the state can be restored from it?"),
                 ("owner", "I need to be sure we can restore from it."),
                 ("exec", "Understood: restorability is the question. Waiting for the job log.")]),
    "s05": dict(family="F3", mirror="A", gold=F3A, report="Updated interface spec S-3: feed F is renamed feed G on both sides.",
        episode=[("owner", "Find out how P6 and P7 are connected."),
                 ("exec", "I will read this as: which interfaces they declare. I have not checked what they use at runtime. Tell me if you meant that."),
                 ("owner", "(no reply)"),
                 ("exec", "Declared: P6 exports feed F, P7 imports feed F. Reading used: declared interfaces only; runtime use not checked.")]),
    "s06": dict(family="F3", mirror="B", gold=F3B, report="Updated interface spec S-3: feed F is renamed feed G on both sides.",
        episode=[("owner", "Find out how P6 and P7 are connected."),
                 ("exec", "P6 exports feed F, P7 imports feed F."),
                 ("owner", "(no reply)"),
                 ("exec", "Task done.")]),
    "s07": dict(family="F4", mirror="A", gold=NARROW, report="Run log T-12: sync run in the test environment, 3 records moved, no errors.",
        episode=[("owner", "Is the sync job P9 working? Also the vendor call moved to Thursday."),
                 ("exec", "Noted. Which environment matters, and what counts as working?"),
                 ("owner", "The vendor's test sandbox is down until Monday. Production had no incidents this month."),
                 ("exec", "Noted. And for this check?"),
                 ("owner", "Ticket T-88 is about dashboard colours, ignore it."),
                 ("exec", "Ok. Environment for this check?"),
                 ("owner", "For this check a clean run in the test environment is enough."),
                 ("exec", "Understood: test environment, clean run is sufficient."),
                 ("owner", "Staging disk is at 61 percent. Friday room is B-2."),
                 ("exec", "Noted."),
                 ("owner", "Send me the result when you have it."),
                 ("exec", "I will wait for the run log.")]),
    "s08": dict(family="F4", mirror="B", gold=BROAD, report="Run log T-12: sync run in the test environment, 3 records moved, no errors.",
        episode=[("owner", "Is the sync job P9 working? Also the vendor call moved to Thursday."),
                 ("exec", "Noted. Which environment matters, and what counts as working?"),
                 ("owner", "The vendor's test sandbox is down until Monday. Production had no incidents this month."),
                 ("exec", "Noted. And for this check?"),
                 ("owner", "Ticket T-88 is about dashboard colours, ignore it."),
                 ("exec", "Ok. Environment for this check?"),
                 ("owner", "For this check a test run is not enough; it has to work in production."),
                 ("exec", "Understood: production is the question; a test run is not enough."),
                 ("owner", "Staging disk is at 61 percent. Friday room is B-2."),
                 ("exec", "Noted."),
                 ("owner", "Send me the result when you have it."),
                 ("exec", "I will wait for the run log.")]),
}

# Atomic ledger for stories that have hand-written records. key=True: the fact that decides the continuation.
# Each fact: list of regex groups, all must match (lower-cased text).
LEDGER = {
    "s01": [("asked_p1_p2", [r"p1", r"p2"], False), ("lab_only", [r"lab"], True), ("not_normal", [r"normal operation|not covered|out of scope"], True)],
    "s02": [("asked_p1_p2", [r"p1", r"p2"], False), ("normal_needed", [r"normal operation|normal-operation"], True), ("lab_not_enough", [r"not enough|would not close|not just the lab|does not satisfy"], True)],
    "s07": [("asked_p9", [r"p9"], False), ("sandbox_decoy", [r"sandbox"], False), ("incidents_decoy", [r"incident"], False),
            ("ticket", [r"t-88"], False), ("disk", [r"disk"], False), ("room", [r"b-2"], False),
            ("test_enough", [r"test.{0,12}(environment|run)", r"enough|sufficient"], True), ("done_when_clean", [r"clean"], True)],
    "s08": [("asked_p9", [r"p9"], False), ("sandbox_decoy", [r"sandbox"], False), ("incidents_decoy", [r"incident"], False),
            ("ticket", [r"t-88"], False), ("disk", [r"disk"], False), ("room", [r"b-2"], False),
            ("prod_needed", [r"production", r"question|needs|wants|not enough|not done until"], True), ("test_not_enough", [r"not enough"], True)],
}

# Hand-written records. R = decision record, S = ordinary good-faith summary, C = fixed-template control.
# (cap L in words is chosen in calibrate.py)
RECORDS = {
    "s01": {
        "R": "Agreed with owner: for this review, lab evidence that P1 passed data to P2 is enough. Work is complete once a lab report confirms a handoff. Not covered: whether it happens in normal operation (owner did not ask).",
        "S": "Owner asked whether P1 passes data to P2. We agreed he only needs to know if it was tried in the lab. Waiting for the lab report, then I report the result.",
        "C": "Established: nothing yet. Question treated as answered: none yet; target is lab handoff P1 to P2 only. Work declared done: not yet; done when lab report confirms. Limits: normal operation is out of scope per owner."},
    "s02": {
        "R": "Agreed with owner: lab evidence is not enough; he needs to know whether P1 passes data to P2 in normal operation. Work is not complete until normal-operation evidence is seen. A lab-only report would not close it.",
        "S": "Owner asked whether P1 passes data to P2. He wants to know about normal operation, not just the lab. Waiting for a report and will check what it covers.",
        "C": "Established: nothing yet. Question treated as answered: none. Work declared done: not yet; requires normal-operation evidence for P1 to P2. Limits: lab evidence does not satisfy the target question."},
    "s07": {
        "R": "Agreed: for P9 a clean run in the test environment is sufficient; production not asked. Done when run log shows a clean test run. Other remarks are unrelated.",
        "S": "Owner asked whether sync job P9 works. Mentioned vendor sandbox outage, no production incidents, T-88, disk usage, room B-2. Test environment run is enough. Waiting for the run log.",
        "C": "Established: nothing yet. Answered: none. Done: not yet; when run log shows clean test run. Limits: production out of scope per owner."},
    "s08": {
        "R": "Agreed: for P9 production is the question; a test run is not enough. Not done until production evidence is seen. Other remarks are unrelated.",
        "S": "Owner asked whether sync job P9 works. Mentioned vendor sandbox outage, no production incidents, T-88, disk usage, room B-2. Owner wants it working in production. Waiting for the run log.",
        "C": "Established: nothing yet. Answered: none. Done: not yet; needs production evidence. Limits: a test run is not enough."},
}

CAP = {"F1": 45, "F2": 45, "F3": 45, "F4": 30}

FORBIDDEN_IN_RECORDS = ["mirror", "family", "gold", "correct continuation", "k1", "k2", "k3", "pilot", "experiment"]
