count = 1
tasks = []


def welcome():
    print("///////Welcome////////")
    print("----------------------")

def help_command():
    print("//////HELP//////")
    print("> Options:")
    print("(list, view, create, update, delete)")
    print("----------------------")

def list_command():
    for task in tasks:
        print(f'> {task["id"]}: {task["name"]}')
        print("----------------------")

def navigation():
    global count
    options = input("> Choose an option: ")
    print("----------------------")
    if options.lower() == "list":
        list_command()
    if options.lower() == "view":
        view_command()
    if options.lower() == "create":
        x = create_commnad()
        tasks.append(x)
        count += 1
    if options.lower() == "update":
        update_command()                 
    if options.lower() == "delete":
        print("////IN PROGRES////")
    else: help_command()
    
        
def view_command():
    view_task = int(input("> Choose a task: "))
    print("----------------------")
    for task in tasks:
        if task["id"] == view_task:
            print("> Task",task["id"])
            print(f'- Nombre: {task["name"]}\n- Description: {task["description"]}\n- Date: {task["date"]}\n- Assignee: {task["assignee"]}')
            print("----------------------")
        
def create_commnad():
    create = {"id" : count,"name" : input("> Name of the task: "), "description": input("> description: "), "date" :input("> Date: "), "assignee": input("> Assignee: ")}
    print("----------------------")
    return create

def update_command():
    update_task = int(input("> Choose a task: "))
    for task in tasks:
        if task["id"] == update_task:
            print("> Task",task["id"])
            print(f'- Nombre: {task["name"]}\n- Description: {task["description"]}\n- Date: {task["date"]}\n- Assignee: {task["assignee"]}')
            print("----------------------")
            print("> What do you want to update? ")
            print("(name, description, date, assignee)")
            print("----------------------")
            options = input("> Choose an option: ")
            print("----------------------")
            if options.lower() == "name":
                update = input("New name: ")
                print("----------------------")
                task["name"] = update
            if options.lower() == "description":
                update = input("New description: ")
                print("----------------------")
                task["description"] = update
            if options.lower() == "date":
                update = input("New date: ")
                print("----------------------")
                task["date"] = update
            if options.lower() == "assignee":
                update = input("New assignee: ")
                print("----------------------")
                task["assignee"] = update
            
            else: help_command()

welcome()       
while True:
    navigation()
    