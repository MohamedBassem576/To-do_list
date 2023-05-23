
todo_list = []


def add_item():
    item = input("Enter a to-do item: ")
    todo_list.append(item)
    print("Item added successfully!")

def remove_item():
    if len(todo_list) == 0:
        print("The to-do list is empty.")
    else:
        print("Current to-do items:")
        for i, item in enumerate(todo_list, start=1):
            print(f"{i}. {item}")
        item_index = int(input("Enter the index of the item to remove: ")) - 1
        if 0 <= item_index < len(todo_list):
            removed_item = todo_list.pop(item_index)
            print(f"Item '{removed_item}' removed successfully!")
        else:
            print("Invalid index.")


def display_list():
    if len(todo_list) == 0:
        print("The to-do list is empty.")
    else:
        print("Current to-do items:")
        for i, item in enumerate(todo_list, start=1):
            print(f"{i}. {item}")


def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Quit")


while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
