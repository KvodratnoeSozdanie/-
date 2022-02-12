import random
import time
mine=[6, 7, 8, 9, 10, 11, 2, 3, 4]*4+['шоколадка']
random.shuffle(mine)
#print(craft)
print('сыграем в игру?')
tvoi_ochko=0
bot_ochko=0
s_k=0
h=1
s=0
r=1
q=1
while True:
                tvoi_vibor=input('берешь шоколадку?, Да/Нет: ')
                if tvoi_vibor=='Да':
                                #craft=random.choice(mine) print(mine)
                                craft=random.choice(mine)
                                print('Тебе не повезло с картой:',craft)
                                tvoi_ochko=tvoi_ochko+craft
                                print('Твои копейки:',tvoi_ochko)
                if tvoi_ochko>21:
                                print('Social credit -100')
                                s_k=s_k-100
                                tvoi_ochko=0
                                bot_ochko=0
                if tvoi_ochko==21:
                                print('Social credit +10')
                                s_k=s_k+10
                                tvoi_ochko=0
                                bot_ochko=0
                if tvoi_vibor=='social credit':
                                print(s_k)
                if tvoi_vibor=='Нет' and tvoi_ochko<21:
                              print('Твои копейки:',tvoi_ochko)
                              print('Ход бота')
                              while True:
                                      
                                           craft=random.choice(mine)
                                           print('Овощь выбрал карту:',craft)
                                           bot_ochko=bot_ochko+craft
                                           print('Рубли овоща:',bot_ochko)
                                           if bot_ochko<tvoi_ochko:
                                                   r=0
                                           if bot_ochko==tvoi_ochko:
                                                   r=1
                                           if bot_ochko>tvoi_ochko:
                                                   r=1
                                           d=int(bot_ochko/21*10)
                                           s=['da']*int(tvoi_ochko/21*10)+['net']*d*r
                                           k=random.choice(s)
                                           if bot_ochko>21:
                                                        print('Бот проиграл! Ты выиграл!')
                                                        print('Social credit +10')
                                                        s_k=s_k+10
                                                        tvoi_ochko=0
                                                        bot_ochko=0
                                                        break
                                           if bot_ochko==21:
                                                        print('Бот выиграл!')
                                                        bot_ochko=0
                                                        print('Social credit -100')
                                                        s_k=s_k-100
                                                        tvoi_ochko=0
                                                        bot_ochko=0
                                                        break
                                           
                                                   
                                                
                                           if k=='net':
                                                    if bot_ochko>tvoi_ochko and bot_ochko<21:
                                                            print('Social credit -100')
                                                            s_k=s_k-100
                                                            tvoi_ochko=0
                                                            bot_ochko=0
                                                            break
                                                            
                                                    if bot_ochko<tvoi_ochko:
                                                                print('Social credit +10')
                                                                s_k=s_k+10
                                                                tvoi_ochko=0
                                                                bot_ochko=0
                                                                break
                                                            
                                           if k=='da':
                                                        print('Овощь берёт карту!')
                                                        time.sleep(1)
                                           
                                                       
                if tvoi_vibor=='КНБ':
                            a=['камень', 'ножницы', 'бумага', 'камень', 'ножницы', 'бумага',  'шоколадка']
                            while True:
                                    v=input('Хочешь поиграть в камень ножницы бумага?Выбирай!, К/Н/Б')
                                    b=random.choice(a)
                                    if v=='К':
                                            if b=='ножницы':
                                                    print('бот выбрал ножницы! Ты выиграл!')
                                            if b=='бумага':
                                                    print('бот выбрал бумагу! Ты проиграл!')
                                            if b=='камень':
                                                    print('бот тоже выбрал камень! Ничья!')
                                            if b=='шоколадка':
                                                     print('бот хочет шоколадку!')
                                    elif v=='Н':
                                            if b=='ножницы':
                                                    print('бот тоже выбрал ножницы! Ничья!')
                                            if b=='бумага':
                                                    print('бот выбрал бумагу! Ты выиграл!')
                                            if b=='камень':
                                                   print('бот выбрал камень! Ты проиграл')
                                            if b=='шоколадка':
                                                    print('бот хочет шоколадку!')
                                    elif v=='Б':
                                            if b=='ножницы':
                                                    print('бот выбрал ножницы! Ты проиграл!')
                                            if b=='бумага':
                                                    print('бот тожу выбрал бумагу! Ничья')
                                            if b=='камень':
                                                    print('бот выбрал камень! Ты выиграл!')
                                            if b=='шоколадка':
                                                    print('бот хочет шоколадку!')

                                    elif v=='kvadrat':
                                            print('Игра сдохла! Пока!')
                                            break
                                    else:
                                            print('Пиши К Н или Б то есть камень ножницы или бумага')

