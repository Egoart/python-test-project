import time
import datetime
import os
import draw_num


count = 0

def get_current_time():
    return datetime.datetime.now().strftime("%H%M%S")


    
def separator_condition(count):
    if count%2 == 0:
        return draw_num.sep_collect[1]
    else: return draw_num.sep_collect[3]



while True:

    count += 1
    
    sep_chain = separator_condition(count)

    #get time string
    var = get_current_time()
    
     

    #output clock strings
    for i in range(5):
        hours_str = draw_num.num_collect[var[0]][i] + ' ' + draw_num.num_collect[var[1]][i] 
        separator = sep_chain[i]
        minutes_str = draw_num.num_collect[var[2]][i] + ' ' + draw_num.num_collect[var[3]][i]
        seconds_str = draw_num.num_collect[var[4]][i] + ' ' + draw_num.num_collect[var[5]][i]
        print(hours_str + separator + minutes_str + separator + seconds_str)
    
       
    #sleep and clear screen
    time.sleep(1)
    os.system('cls')