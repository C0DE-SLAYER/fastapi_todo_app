def indi_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "desc": todo["desc"],
        "complete": todo["complete"]
    }

def multi_serial(todos) -> list:
    return [indi_serial(todo) for todo in todos]