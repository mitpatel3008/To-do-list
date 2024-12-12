def task():
    tasks=[]
    print('----WELCOME TO TASK MANAGEMENT APP----\n')
    total_task=int(input("Enter how many task you want to add : "))

    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} : ")
        tasks.append(task_name)
    print("\n")
    print(f"Your today's tasks are\n{tasks}\n")

    while True:
        operation=int(input("Enter 1: Add\nEnter 2: Update\nEnter 3: Delete\nEnter 4: View\nEnter 5: Exit/Stop\n\n"))
        if operation==1:
            add=input("Enter the task you want to add : ")
            tasks.append(add)
            print(f"Task {add} has been added...\n")

        elif operation==2:
            updated_task=(input("Enter the task name you want to update : "))
            if updated_task in tasks:
                up=input("Enter new task : ")
                index=tasks.index(updated_task)
                tasks[index]=up
                print(f"Task {up} has been updated...\n")
            else:
                print(f"{updated_task} not found...\n")

        elif operation==3:
            dtask=input("Enter the task you want to delete : ")
            if dtask in tasks:
                index=tasks.index(dtask)
                tasks.pop(index)
                print(f"Task {dtask} has been deleted...\n")

        elif operation==4:
            print(f"Your today's tasks are :\n{tasks}\n")

        elif operation==5:
            print("You are outside the program.")
            break

        else:
            print("Enter valid input :")
       
task()