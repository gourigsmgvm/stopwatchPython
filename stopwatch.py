import time
t = 100
while(t > -1):
    m = t//60
    s = t%60
    time.sleep(1)
    print(m ,":", s)
    t = t-1
 
