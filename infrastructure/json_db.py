import json

def load_json():
    with open("infrastructure/tasks.json") as f:
        return json.loads(f.read())

db = load_json()
tasks = db["tasks"]
counter = db["counter"]

def overwrite():
    with open("infrastructure/tasks.json", "w") as f:
        f.write(json.dumps({"tasks":tasks ,"counter":counter}))
 
def save(task):
    existing_task = find(task["id"])
    if existing_task is not None:
        existing_task["name"] = task["name"]
        existing_task["description"] = task["description"]
        existing_task["date"] = task["date"]
        existing_task["assignee"] = task["assignee"]
    tasks.append(task)
    overwrite()

def find(id):
    for task in tasks:
        if task["id"] == id:
            return task
    raise ValueError(f"Task with id: '{id}' not found")

def delete(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            overwrite()

def search():
    return tasks
