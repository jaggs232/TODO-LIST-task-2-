tasks = []


try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    pass  

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Show tasks")
    print("2. Add task") 
    print("3. Remove task")
    print("4. Quit")
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added!")
    
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            
            task_num = input("Which task to remove? (enter number): ")
            task_num = int(task_num) - 1
            
            if task_num >= 0 and task_num < len(tasks):
                removed = tasks.pop(task_num)
                print(f"Removed: {removed}")
            else:
                print("Invalid number!")
    
    elif choice == "4":
        file = open("tasks.txt", "w")
        for task in tasks:
            file.write(task + "\n")
        file.close()
        print("Tasks saved. Goodbye!")
        break