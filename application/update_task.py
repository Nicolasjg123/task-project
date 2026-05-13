from infrastructure import json_db as db

statuses = ["TODO", "IN_PROGRESS", "DONE"]

def execute(id, name = None,description = None, date = None, assignee = None, status = None):
    task = db.find(id)
    if task is not None:
        if name is not None:
            task["name"] = name
        if description is not None:
            task["description"] = description
        if date is not None:
            task["date"] = date
        if assignee is not None:
            task["assignee"] = assignee
        if status is not None:
            if status in statuses:
                task["status"] = status
            else:
                raise ValueError(f"Status '{status}' is invalid")
        return db.save(task)

    raise ValueError (f"Task with id: '{id}' not found")
    