user_name = input('Enter user name ')

def deposit_income(principal, rate, period):
    return int(principal * rate * period)

def user_name_control (fun):
    def wrapper_user_name_control (principal, rate, period):
        if user_name == 'admin':
           result = 'Your annual income ' + str(fun(principal, rate, period)) +'$'
           return result
        else: return 'You are not allowed to view this'
    return wrapper_user_name_control


deposit_income = user_name_control(deposit_income) 
output = deposit_income(100, 0.05, 1)
print (output)

