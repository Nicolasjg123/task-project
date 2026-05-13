from infrastructure import json_db

def execute(id):
    json_db.delete(id)
