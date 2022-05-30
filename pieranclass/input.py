x,y,z = [int (x) for x in input ("Enter three number").split(",")]
print("first number is {} and Second number is {} and third number is {}".format(x,y,z))

import time
count_second = 10
for i in reversed(range(count_second + 1)):
    if i > 0:
        print(i,end='>>>')
        time.sleep(1)
    else:
        print('Start')
