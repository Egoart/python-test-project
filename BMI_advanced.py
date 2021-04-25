import process_user

#Show menu
def show_menu():
    MENU = """
    1. Add new user 
    2. Show all users in the list
    3. Show user data
    4. Edit user data
    5. Delete user
    6. Exit
    """
    print(MENU)

#Dictionary for choosing option
ACTIONS = {
    1: process_user.create_user,
    2: process_user.list_users,
    3: process_user.read_user,
    4: process_user.update_user,
    5: process_user.delete_user
}

#Function to launch user processing function
def select_action(answer):
    action = ACTIONS.get(answer, show_menu)  
    action()

#Function for indefinite loop to show user menu and ask for the option
def main():    
    while True:
        show_menu()
        answer = int(input('Select an option: '))      
        if answer == 6:
            print()
            print('Bye')
            print()
            break
        select_action(answer)

main()