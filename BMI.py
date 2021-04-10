#PART I - FIND THE NUMERIC VALUE OF BMI
body_mass = input('Enter your body weight in kg ')
height = input ('Enter your height in cm ')

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
bmi_indicator_position = bmi - int(bmi_start_value)
bmi_tail_lenght = int(bmi_end_value) - int(bmi_start_value) - 1 - bmi_indicator_position
bmi_tail_line = '=' * bmi_tail_lenght
bmi_processed_line = bmi_raw_line[1:bmi_indicator_position] + '!' + bmi_tail_line

#generate BMI scale with indicator and terminal values
bmi_refernce_full_scale = bmi_start_value + bmi_raw_line + bmi_end_value
bmi_full_scale = bmi_start_value + bmi_processed_line + bmi_end_value

#test conformity
#print (bmi_refernce_full_scale) 
print (bmi_full_scale)
print()


