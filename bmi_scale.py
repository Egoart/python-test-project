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