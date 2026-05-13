from infrastructure import json_db

def execute(id):
    return json_db.find(id)
