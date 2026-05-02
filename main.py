import json

def load_tasks():
    with open("tasks.json") as f:
        return json.loads(f.read()) ["tasks"] 

def load_count():
    with open("tasks.json") as f:
        return json.loads(f.read())["count"]

tasks = list(load_tasks())
count = load_count()




def save():
    with open("tasks.json", "w") as f:
        f.write(json.dumps({"tasks": tasks, "count": count}))


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
    print("----------------------") 
    confirm = input("> Do you want to save the task?: ") 
    print("----------------------")
    print(type(tasks))
    if confirm.lower() == "yes":
        print("> Task saved")
        print("----------------------")
        tasks.append(create)
        count += 1
        save()
    if confirm.lower() == "no":
            navigation()
    

def update_command():
    list_command()
    for task in tasks:
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
                confirm = input ("> Are you sure?: ")
                if confirm.lower() == "yes":
                    task["name"] = update
                    save()
                if confirm.lower() == "no":
                    navigation()
            if options.lower() == "description":
                update = input("> New description: ")
                print("----------------------")
                confirm = input (">Are you sure?: ")
                if confirm.lower() == "yes":
                    task["description"] = update
                    save()
                if confirm.lower() == "no":
                    navigation()
            if options.lower() == "date":
                update = input("> New date: ")
                print("----------------------")
                confirm = input (">Are you sure?: ")
                if confirm.lower() == "yes":
                    task["date"] = update
                    save()
                if confirm.lower() == "no":
                    navigation()
            if options.lower() == "assignee":
                update = input("> New assignee: ")
                print("----------------------")
                confirm = input ("> Are you sure?: ")
                if confirm.lower() == "yes":
                    task["assignee"] = update
                    save()
                if confirm.lower() == "no":
                    navigation()
            else: help_command()


def delete_command():
    list_command()
    delete_task = int(input("> Choose a task: "))
    print("----------------------")
    for task in tasks:
        if task["id"] == delete_task:
            confirm = input("Are you sure you want to delete the task?: ")
            if confirm.lower() == "yes":
                tasks.remove(task)
                save()
            if confirm.lower() == "no":
                navigation()

welcome()
help_command()

while True:
    z = navigation()
    if z == "exit":
        break
