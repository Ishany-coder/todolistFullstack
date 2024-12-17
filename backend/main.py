todoList = []
print("Welcome to the todo list!")

def handle_invalid_input():
    print("Invalid input. Please enter 'add', 'remove', 'show', or 'break'.")

def AskAddOrRemove():
    AddOrRemove = input("Would you like to add or remove a task? (add/remove) ")
    return AddOrRemove

def add_task(task):
    print("In add_task")
    todoList.append(task)
    print(f"Task '{task}' added to the todo list.")
    return todoList

def remove_task(task):
    if task in todoList:
        todoList.remove(task)
        print(f"Task '{task}' removed from the todo list. ")
    else:
        print(f"Task '{task}' not found in the todo list. ")
        new_task = input("please enter a different task to remove: ")
        remove_task(new_task)

def show_list():
    for task in todoList:
        print(task)

    
# def main():
#     while True:
#         print("In main.py")
#         RemoveOrAdd = AskAddOrRemove()
#         if RemoveOrAdd == "add":
#             task = input("Enter the task you would like to add: ")
#             add_task(task)
#         elif RemoveOrAdd == "remove":
#             task = input("Enter the task you would like to remove: ")
#             remove_task(task)
#         elif RemoveOrAdd == "show":
#             show_list()
#         elif RemoveOrAdd == "break":
#             break
#         else:
#             handle_invalid_input()

# main()

print("Thank you for using the todo list!")
