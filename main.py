count = 3
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
    return input("Choose an option: ")
options = navigation()
    
welcome()

if options == "1":
    print("Yeyyy")