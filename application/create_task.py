from infrastructure import json_db

def execute(task):
    json_db.save(task)
