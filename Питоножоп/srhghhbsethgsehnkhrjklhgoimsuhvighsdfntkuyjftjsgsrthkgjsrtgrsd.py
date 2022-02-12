d=int(input('введи кол-во вариантов кваса:'))
j=0
for i in range(d):
             g=int(input('вв:'))
             if g%5==0 and g>j:
                          j=g
print(j)
