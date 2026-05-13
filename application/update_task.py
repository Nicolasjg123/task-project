from infrastructure import json_db

def execute(id, name = None,description = None, date = None, assignee = None):
    task = json_db.find(id)
    if task is not None:
        task["name"] = name
        task["description"] = description
        task["date"] = date
        task["assignee"] = assignee
        return json_db.save(task)

    raise ValueError (f"Task with id: '{id}' not found")
    
 