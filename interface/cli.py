from application import create_task
from application import update_task
from application import find_task

def welcome():
    print("----------------------")
    print("///////Welcome CLI////////")
    print("----------------------")

def success():
    print("///////Success////////")

def create_command():
    name = input("> Name of the task: ")
    description =input("> description: ")
    date =input("> Date: ")
    assignee = input("> Assignee: ")
    print("----------------------") 
    while True: 
        confirm = input("> Do you want to save the task? yes/no: ") 
        print("----------------------")
        if confirm.lower() == "yes":
            create_task.execute(name = name, description = description, date = date, assignee = assignee)
            print("> Task saved")
            print("----------------------")
            break
        if confirm.lower() == "no":
            navigation() 
            break

def update_command():
    id = input("> Choose a task: ")
    task = find_task.execute(id)
    print("> Task",task["id"])
    print("----------------------")
    print(f'- Nombre: {task["name"]}\n- Description: {task["description"]}\n- Date: {task["date"]}\n- Assignee: {task["assignee"]}')
    print("----------------------")
    print("> What do you want to update? ")
    print("(name, description, date, assignee, status)")
    print("----------------------")

    option = input("> Choose an option: ").lower()
    print("----------------------")

    if option == "name":
        new_name = input("> New name: ")
        print("----------------------")
        confirm = input ("> Are you sure?: ")
        if confirm.lower() == "yes":
            update_task.execute(id = id, name = new_name)
            success()

    elif option == "description":
        new_description = input("> New description: ")
        print("----------------------")
        confirm = input (">Are you sure?: ")
        if confirm.lower() == "yes":
            update_task.execute(id = id, description = new_description)
            success()
        
    elif option == "date":
        new_date = input("> New date: ")
        print("----------------------")
        confirm = input (">Are you sure?: ")
        if confirm.lower() == "yes":
            update_task.execute(id = id, date = new_date)
            success()
    elif option == "assignee":
        new_assignee = input("> New assignee: ")
        print("----------------------")
        confirm = input ("> Are you sure?: ")
        if confirm.lower() == "yes":
            update_task.execute(id = id, assignee = new_assignee)
            success()
    elif option == "status":
        new_status = input("> New status: ")
        print("----------------------")
        confirm = input ("> Are you sure?: ")
        if confirm.lower() == "yes":
            update_task.execute(id = id, status = new_status)
            success()
        
    else:
        help_command()



def help_command():
    print("//////HELP//////")
    print("> Options:")
    print("(list, view, create, update, delete, exit)")
    print("----------------------")

def navigation():
    while True:
        options = input("> Choose an option: ")
        print("----------------------")
        if options.lower() == "list":
            pass
        elif options.lower() == "view":
            pass
        elif options.lower() == "create":
            create_command()
        elif options.lower() == "update":
            update_command()
        elif options.lower() == "delete":
            pass
        elif options.lower() == "exit":
            break
        else: 
            help_command()

def start():
    welcome()
    navigation()