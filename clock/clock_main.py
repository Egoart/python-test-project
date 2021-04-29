import time
import datetime
import os
import num_collection


def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


while True:
    #counter for jumping dots
    num_collection.count += 1
    
    #get nested list based on current time str value
    list_out = num_collection.numbers_collection(get_current_time())
    
    #output list 
    for i in range(5):
        for j in range(len(list_out)):
            for k in range(3):
                print(list_out[j][i][k], end='')
            print(end='  ')
        print()
    
    #clear list
    del list_out[:]   
    
    #sleep and clear screen
    time.sleep(1)
    os.system('cls')

  
        



 