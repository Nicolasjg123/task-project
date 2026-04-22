count = 1
tasks = []


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
    global count
    options = input("Choose an option: ")
    if options == "list":
        list_command()
    if options == "view":
        view_command()
    if options == "create":
        x = create_commnad()
        tasks.append(x)
        count += 1
    if options == "update":
        print("////IN PROGRES////")
    if options == "delete":
        print("////IN PROGRES////")
    else: help_command()
    return options
        
def view_command():
    view_task =int(input("Choose a task: "))
    for task in tasks:
        if task["id"] == view_task:
            print(f'Nombre: {task["name"]}\nDescription: {task["description"]}\nDate: {task["date"]}\nAssignee: {task["assignee"]}')
        
def create_commnad():
    create = {"id" : count,"name" : input("Name of the task: "), "description": input("description: "), "date" :input("Date: "), "assignee": input("Assignee: ")}
    return create
   
while True:
    welcome()
    navigation()

    