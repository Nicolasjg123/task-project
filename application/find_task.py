from infrastructure import json_db as db

def execute(id):
    task = db.find(id)
    if task is not None:
        return task
    
    raise ValueError (f"Task with id: '{id}' not found")
