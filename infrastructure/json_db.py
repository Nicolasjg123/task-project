import json

def load_json():
    with open("infrastructure/tasks.json") as f:
        return json.loads(f.read())

db = load_json()
tasks = db["tasks"]

def overwrite():
    with open("infrastructure/tasks.json", "w") as f:
        f.write(json.dumps({"tasks":tasks }))
 
def save(task):
    existing_task = find(task["id"])
    if existing_task is not None:
        existing_task["name"] = task["name"]
        existing_task["description"] = task["description"]
        existing_task["date"] = task["date"]
        existing_task["assignee"] = task["assignee"]
        existing_task["status"] = task["status"]
    else:
        tasks.append(task)
    
    overwrite()

def find(id):
    for task in tasks:
        if task["id"] == id:
            return task

def delete(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            overwrite()

def search():
    return tasks
