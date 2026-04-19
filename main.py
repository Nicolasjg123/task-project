count = 3
tasks = [
    {
        1: {"id":1,
        "name":"gym",
        "description":"Ir al gym",
        "date":"2026-04-17",
        "assignee":"Mike"}
    }, 
    {
        2: {"id":2,
        "name":"work",
        "description":"programming",
        "date":"2026-04-17",
        "assignee":"Nico"}
    },
    {
        3: {"id":3,
        "name":"Play",
        "description":"Play Mario",
        "date":"2026-04-17",
        "assignee":"Jake"}
    },
]

def welcome():
    print("///////Welcome////////")



def help_command():
    print("//////HELP//////")
    print("Options:")
    print("list, view, create, update, delete")


def list_command():
    for task in tasks:
        print(f'{task["id"]}: {task["name"]}')

def navigation():
    options = input("Choose an option: ")
    return options
    
def view_command():
    task =input("Choose a task: ")
    return task
    
navigation()
view_command()
