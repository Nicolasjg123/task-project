from infrastructure import json_db as db

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
            task["status"] = status
        return db.save(task)

    raise ValueError (f"Task with id: '{id}' not found")
    
 