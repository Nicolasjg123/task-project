from infrastructure import json_db as db

def execute(id):
    db.delete(id)
