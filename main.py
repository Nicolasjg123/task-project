count = 0

while True:
    count +=1        
    tasks = [
        {
            "id":1,
            "name":"gym",
            "description":"Ir al gym",
            "date":"2026-04-17",
            "assignee":"Mike"}
        , 
        {
            "id":2,
            "name":"work",
            "description":"programming",
            "date":"2026-04-17",
            "assignee":"Nico"}
        ,
        {
            "id":3,
            "name":"Play",
            "description":"Play Mario",
            "date":"2026-04-17",
            "assignee":"Jake"}
        ,
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
        view_task =int(input("Choose a task: "))
        for task in tasks:
            if task["id"] == view_task:
                print(f'Nombre: {task["name"]}\nDescription: {task["description"]}\nDate: {task["date"]}\nAssignee: {task["assignee"]}')
        
    def create_commnad():
        create = {"id" : count,"name" : input("Name of the task: "), "description": input("description: "), "date" :input("Date: "), "assigee": input("Assignee: ")}
        return create
   
    y = create_commnad()
    print(y)
    