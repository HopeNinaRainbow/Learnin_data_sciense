'''Игра угадай число'''
import numpy as np
number=np.random.randint(1, 101) #загадываем число
#кол-во попыток
count = 0
while True:
    count+=1
    predict_num=int(input("Угадай число от 1 до 100"))
    if predict_num>number:
        print('Число должно быть меньше')
    elif predict_num<number:
        print("Число должно быть больше")
    else:
        print(f'Поздравляю, вы угадали! это число - {number} за {count} попыток')
        break #остановка бесконечного цикла, конец иггры.