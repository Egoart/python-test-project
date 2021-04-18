#PART I - FIND THE NUMERIC VALUE OF BMI
body_mass = input('Enter your body weight in kg ')
height = input ('Enter your height in cm ')

#add another variable -- gender
gender = input ('Answer: Are you male/female/something else? ')

#convert height from cm to meter
height_meters = int(height)/100

#calculate bmi and round to integer
bmi = int(int(body_mass) / (height_meters**2))
print()
print('Your body mass index is', bmi)

# PART II - GRAPHIC REPRESENTATION OF BMI
#Set scale range
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

    #test conformity
    #print (bmi_refernce_full_scale) 
    print (bmi_full_scale)
    print ()
else:
    print ('You have a serious weight problem')

# By gender

if gender == 'female':
    if bmi <= 18:
        print ('You are anorexic. Urgently consult a doctor.')
    elif bmi in range(19, 25):
        print ('You don not have weight problems. Congratulations!')
    elif bmi in range(26, 30):
        print ('You have signs of obesity. Consult a doctor.')
    elif bmi in range(31, 40):
        print ('You are obese. Consult a doctor.')
    else:
        print ('You are extremely obese. Urgently consult a doctor.')
elif gender == 'male':
    if bmi <= 19:
        print ('You are underweight. Urgently consult a doctor.')
    elif bmi in range(20, 27):
        print ('You don not have weight problems. Congratulations!')
    elif bmi in range(28, 33):
        print ('You have signs of obesity. Consult a doctor.')
    elif bmi in range(34, 44):
        print ('You are obese. Consult a doctor.')
    else:
        print ('You are extremely obese. Urgently consult a doctor.')
else:
    print ("The result may not be correct for you. Please find appropriate BMI caulculator.")
    
print ()    



