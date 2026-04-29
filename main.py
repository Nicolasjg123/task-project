count = 1
tasks = []

def welcome():
    print("///////Welcome////////")
    print("----------------------")

def help_command():
    print("//////HELP//////")
    print("> Options:")
    print("(list, view, create, update, delete, exit)")
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
        create_commnad()
        
    if options.lower() == "update":
        update_command()
    if options.lower() == "delete":
        delete_command()
    if options.lower() == "exit":
        return options
    else: help_command()

def list_command():
    for task in tasks:
        print(f'> {task["id"]}: {task["name"]}')
        print("----------------------")

def view_command():
    view_task = int(input("> Choose a task: "))
    print("----------------------")
    for task in tasks:
        if task["id"] == view_task:
            print("> Task",task["id"])
            print(f'- Nombre: {task["name"]}\n- Description: {task["description"]}\n- Date: {task["date"]}\n- Assignee: {task["assignee"]}')
            print("----------------------")

def create_commnad():
    global count
    create = {"id" : count,"name" : input("> Name of the task: "), "description": input("> description: "), "date" :input("> Date: "), "assignee": input("> Assignee: ")}
    print("----------------------") #Translate the confirmacion here
    save = input("> Do you want to save the task?: ") # <- This go to create commnad
    print("----------------------")
    if save.lower() == "yes":
        print("> Task saved")
        print("----------------------")
        tasks.append(create)
        count += 1
    if save.lower() == "no":
            navigation()
    

def update_command():
    for task in tasks:
        print(f'> {task["id"]}: {task["name"]}')
        update_task = int(input("> Choose a task: "))
        if task["id"] == update_task:
            print("> Task",task["id"])
            print("----------------------")
            print(f'- Nombre: {task["name"]}\n- Description: {task["description"]}\n- Date: {task["date"]}\n- Assignee: {task["assignee"]}')
            print("----------------------")
            print("> What do you want to update? ")
            print("(name, description, date, assignee)")
            print("----------------------")
            options = input("> Choose an option: ")
            print("----------------------")
            if options.lower() == "name":
                update = input("> New name: ")
                print("----------------------")
                save = input ("> Are you sure?: ")
                if save.lower() == "yes":
                    task["name"] = update
                if save.lower() == "no":
                    navigation()
            if options.lower() == "description":
                update = input("> New description: ")
                print("----------------------")
                save = input (">Are you sure?: ")
                if save.lower() == "yes":
                    task["description"] = update
                if save.lower() == "no":
                    navigation()
            if options.lower() == "date":
                update = input("> New date: ")
                print("----------------------")
                save = input (">Are you sure?: ")
                if save.lower() == "yes":
                    task["date"] = update
                if save.lower() == "no":
                    navigation()
            if options.lower() == "assignee":
                update = input("> New assignee: ")
                print("----------------------")
                save = input ("> Are you sure?: ")
                if save.lower() == "yes":
                    task["assignee"] = update
                if save.lower() == "no":
                    navigation()
            else: help_command()


def delete_command():
    for task in tasks:
        print(f'> {task["id"]}: {task["name"]}')
        print("----------------------")
        delete_task = int(input("> Choose a task: "))
        print("----------------------")
        if task["id"] == delete_task:
            save = input("Are you sure you want to delete the task?: ")
            if save.lower() == "yes":
                tasks.remove(task)
            if save.lower() == "no":
                navigation()

welcome()
help_command()

while True:
    z = navigation()
    if z == "exit":
        break
