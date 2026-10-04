TOOLS = ["explain", "suggest_index"]
WRITES = ("insert", "delete", "drop", "truncate",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = "Seq Scan" if "select" in goal.lower() else "unknown"
    return {"refused": False, "tools": TOOLS, "plan": result, "wrote": False, "applied": False}
