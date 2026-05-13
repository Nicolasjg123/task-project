from application import create_task
from application import delete_task
from application import find_task
from application import search_tasks
from application import update_task
#create_task.execute({"id": 4, "name": "Play", "description": "Fortnite", "date": "5/9/26", "assignee": "Gus"})
#delete_task.execute(4)
#task = find_task.execute(200)
#print(task)
#task = search_tasks.execute()
#print(task)

create_task.execute(name = "Gym", description = "Go to the gym", date = "5/15/26", assignee = "Mike")