box_element = '\u2B1C'

count = 0

# define empty list
list_numbers = []

# Compose and return nested list with numbers corresponding to current time str
def numbers_collection(num):
    
    for i in range(len(num)):

        if num[i] == ':':
            if count%2 != 0:
                get_сolon = [['  ' for i in range(3)] for j in range(5) ]
                for row in range(5):
                    for col in range(3):
                        if col == 1 and row == 1:
                            get_сolon[row][col] = box_element
                list_numbers.append(get_сolon)
            else:
                get_сolon = [['  ' for i in range(3)] for j in range(5) ]
                for row in range(5):
                    for col in range(3):
                        if col == 1 and row == 3:
                            get_сolon[row][col] = box_element
                list_numbers.append(get_сolon)

        # Zero
        elif num[i] == '0':
            get_zero = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if (col == 0 or col == 2) or (row == 0 or row == 4):
                        get_zero[row][col] = box_element
            list_numbers.append(get_zero)

        # One
        elif num[i] == '1':
            get_one = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if (col == 2 or row == 0) and col != 0:
                        get_one[row][col] = box_element
            list_numbers.append(get_one)

        # Two
        elif num[i] == '2':
            get_two = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if row == 0 or row == 2 or (col == 0 and row == 3) or row == 4 or (row == 1 and col == 2):
                        get_two[row][col] = box_element
            list_numbers.append(get_two)

        # Three
        elif num[i] == '3':
            get_three = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if col == 2 or (row == 0 or row == 2 or row == 4):
                        get_three[row][col] = box_element
            list_numbers.append(get_three)

        # Four
        elif num[i] == '4':
            get_four = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if col == 2 or (col == 0 and (row != 3 and row != 4)) or (row == 2):
                        get_four[row][col] = box_element
            list_numbers.append(get_four)

        # Five
        elif num[i] == '5':
            get_five = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if row == 0 or row == 2 or (col == 0 and row == 1) or row == 4 or (row == 3 and col == 2):
                        get_five[row][col] = box_element
            list_numbers.append(get_five)

        # Six
        elif num[i] == '6':
            get_six = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if col == 0 or row == 0 or row == 2 or row == 4 or (col == 2 and row == 3):
                        get_six[row][col] = box_element
            list_numbers.append(get_six)

        # Seven
        elif num[i] == '7':
            get_seven = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if row == 0 or (col == 1 and row > 2) or (col == 2 and row == 1) or (col == 1 and row == 2):
                        get_seven[row][col] = box_element
            list_numbers.append(get_seven)

        # Eight
        elif num[i] == '8':
            get_eight = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if (col == 0 or col == 2) or (row == 0 or row == 4 or row == 2):
                        get_eight[row][col] = box_element
            list_numbers.append(get_eight)

        # Nine
        elif num[i] == '9':
            get_nine = [['  ' for i in range(3)] for j in range(5) ]
            for row in range(5):
                for col in range(3):
                    if col == 2 or (col == 0 and (row != 3 and row != 4)) or row == 0 or row == 2:
                        get_nine[row][col] = box_element
            list_numbers.append(get_nine)

        else: print('Wrong data')            

    return list_numbers    

