import random
import time
print('дай мне квас!')
j=random.randint(0,10)
y=[0]
l=0
p=0
for h in range(j):
                y.append(float(input('кол-во литров:')))
                if y[-1]>=10 and y[-1]<100:
                             print('ты где такую валыну с квасом взял?')
                if y[-1]>=100:
                             time.sleep(3)
                             print('ты явно пытаешься меня обмануть! Таких больших бутылок кваса не существует!')
                             time.sleep(3)
                             print('я убегаю с твоим квасом в закат своровав',sum(y),'литров твоего кваса!*')
                             break
                print('вливаю твой квас себе в бутылку*')
                print('у меня ',sum(y),' литров твоего кваса')
                time.sleep(3)
print('я своровал у тебя ',sum(y),' литров кваса')
time.sleep(5)
print('я убежал с твои квасом в Казахстан*')
