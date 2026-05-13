import uuid
from infrastructure import json_db as db

def execute(name, description, date, assignee):
    task = {
        "id": str(uuid.uuid4()),
        "name" : name,
        "description" : description,
        "date" : date,
        "assignee" : assignee,
        "status" : "TODO"
    }
    db.save(task)


