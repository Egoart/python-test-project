import time
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%H%M%S")
    

t = get_current_time()

print(type(t))

k=0

while True:
    k += 1
    if k%2 !=0:
        print('odd')
    else: print('even')
    
    if k == 10:
        break