count = 0

tasks = [
    {
        "id":1,
        "name":"gym",
        "description":"Ir al gym",
        "date":"2026-04-17",
        "assignee":"Mike"
    }, 
    {
        "id":2,
        "name":"work",
        "description":"programming",
        "date":"2026-04-17",
        "assignee":"Nico"
    },
    {
        "id":3,
        "name":"Play",
        "description":"Play Mario",
        "date":"2026-04-17",
        "assignee":"Jake"
    },
]

print("///////Welcome////////")



def help_command():
    print("//////HELP//////")
    print("Options:")
    print("Tasks, Create, Update, Delete")


def list_command():
    for task in tasks:
        print(f'{task["id"]}: {task["name"]}')

list_command()