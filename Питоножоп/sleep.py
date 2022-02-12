import random
import time
s=0
m=0
h=0
d=0
while True:
             for d in range(24):
                          for h in range(60):
                                       for m in range(60):
                                                    for s in range(60):
                                                                 print(d,':',h,':',m,':',s,)
                                                                 time.sleep(0.001)
