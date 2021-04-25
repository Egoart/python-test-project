import bmi_scale

#Define dictionary to store user data
USER_DATA = {}

#Define function for updating USER_DATA dictionary with new data
def user_data_dictionary_filling(user_name, body_mass, height, gender):
    #Call function for BMI scale generation
    bmi_data = bmi_scale.generate_bmi_scale(body_mass, height)
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