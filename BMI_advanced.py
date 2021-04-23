
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

#Define dictionary to store user data
USER_DATA = {}

#Define function for BMI scale generation
def generate_bmi_scale(body_mass, height):
    #Calculate BMI
    height_meters = int(height)/100
    bmi = int(int(body_mass) / (height_meters**2))

    #Create BMI scale
    bmi_start_value = '15'
    bmi_end_value = '55'

    #calculate the number of filling elements 
    element_number = int(bmi_end_value) - int(bmi_start_value) - 1 
    bmi_raw_line = '=' * element_number

    #find the position of BMI on the scale and generate scale with indicator
    if bmi in range(16, 54):
        bmi_indicator_position = bmi - int(bmi_start_value)
        bmi_processed_line = bmi_raw_line[1:bmi_indicator_position] + '!' + bmi_raw_line[bmi_indicator_position:]

    #generate BMI scale with indicator and terminal values
        bmi_refernce_full_scale = bmi_start_value + bmi_raw_line + bmi_end_value
        bmi_full_scale = bmi_start_value + bmi_processed_line + bmi_end_value
        return bmi_full_scale
    else: return 'You have serious weight problems'
#End of function for BMI scale generation

#Define function for updating USER_DATA dictionary with new data
def user_data_dictionary_filling(user_name, body_mass, height, gender):
    #Call function for BMI scale generation   
    bmi_data = generate_bmi_scale(body_mass, height)
    #Add new data to the USER_DATA dictionary
    USER_DATA[user_name] = {'Mass': body_mass, 'Height': height, 'Gender': gender, 'BMI scale': bmi_data}

        
# Process users
def create_user():
    #Ask for user data
    user_name = input('Enter username ')
    if user_name in USER_DATA:
        return print(f'The name \' {user_name} \' is already taken. Start again and choose another username')
    body_mass = input('Enter body weight in kg ')
    height = input ('Enter height in cm ')
    gender = input ('Enter gender ') 
    user_data_dictionary_filling(user_name, body_mass, height, gender)
    

def list_users():
    print()
    print(list(USER_DATA.keys()))

def read_user():
    user_name = input('Enter username ')
    if user_name not in USER_DATA:
        return print(f'User \' {user_name} \' does not exist. Try another one')
    print()
    user_spec_data = USER_DATA[user_name]
    print(f'User \' {user_name} \' has the following parameters ', user_spec_data)

def update_user():
    user_name = input('Enter the username, whose data you are going to update: ')
    if user_name not in USER_DATA:
        return print(f'User \' {user_name} \' does not exist. Try another one')
    body_mass = input('Enter body weight in kg ')
    height = input ('Enter height in cm ')
    gender = input ('Enter gender ') 
    user_data_dictionary_filling(user_name, body_mass, height, gender)
    user_spec_data = USER_DATA[user_name]
    print (f'User \' {user_name} \' is updated the following parameters', user_spec_data)


def delete_user():
    user_name = input('Enter the username you are going to delete: ')
    if user_name not in USER_DATA:
        return print(f'The user \' {user_name} \' does not exist. Try another one')
    del USER_DATA[user_name]
    print (f'The user \' {user_name} \' is deleted.')


#Dictionary for choosing option
ACTIONS = {
    1: create_user,
    2: list_users,
    3: read_user,
    4: update_user,
    5: delete_user
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