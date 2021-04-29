# Draw zero

box_element = '\u2B1C'

def num_zero():
    for row in range(5):
        for col in range(3):
            if (col == 0 or col == 2) or (row == 0 or row == 4):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_zero()
print()

def num_one():
    for row in range(5):
        for col in range(3):
            if (col == 2 or row == 0) and col != 0:
                print(box_element, end='')
            else: print(end='  ')
        print()

num_one()
print()

def num_two():
    for row in range(5):
        for col in range(3):
            if row == 0 or row == 2 or (col == 0 and row == 3) or row == 4 or (row == 1 and col == 2):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_two()
print()

def num_three():
    for row in range(5):
        for col in range(3):
            if col == 2 or (row == 0 or row == 2 or row == 4):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_three()
print()

def num_four():
    for row in range(5):
        for col in range(3):
            if col == 2 or (col == 0 and (row != 3 and row != 4)) or (row == 2):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_four()
print()

def num_five():
    for row in range(5):
        for col in range(3):
            if row == 0 or row == 2 or (col == 0 and row == 1) or row == 4 or (row == 3 and col == 2):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_five()
print()

def num_six():
    for row in range(5):
        for col in range(3):
            if col == 0 or row == 0 or row == 2 or row == 4 or (col == 2 and row == 3):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_six()
print()

def num_seven():
    for row in range(5):
        for col in range(3):
            if row == 0 or (col == 1 and row > 2) or (col == 2 and row == 1) or (col == 1 and row == 2):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_seven()
print()

def num_eight():
    for row in range(5):
        for col in range(3):
            if (col == 0 or col == 2) or (row == 0 or row == 4 or row == 2):
                print(box_element, end='')
            else: print(end='  ')
        print()

num_eight()
print()

def num_nine():
    for row in range(5):
        for col in range(3):
            if col == 2 or (col == 0 and (row != 3 and row != 4)) or row == 0 or row == 2:
                print(box_element, end='')
            else: print(end='  ')
        print()

num_nine()
print()

def colon():
    for row in range(5):
        for col in range(1):
            if row == 1 or row == 3:
                print(box_element, end='')
            else: print(end='  ')
        print()

colon()
print()








