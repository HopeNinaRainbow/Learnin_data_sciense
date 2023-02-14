'''Игра "угадай число". Компьютер сам загадывает, сам отгадывает.'''
import numpy as np
def random_predict(number:int=1) -> int:
    """_summary_

    Args:

    Returns:
        int: _description_
    """
    count=0
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number==predict_number:
            break
    return count #Это мы посчитали сколько походов комп выполняет для угадывания 1 числа

#А здесь мы его просим тыщу раз провернуть кульбит и просчитать среднее кол-во затраченных попыток
def score_game(random_predict) -> int: #Ф-я от ф-и random_predict(), которая возвращала кол-во подходов для угадыв-я одного числа.
    """_summary(за какое кол-во попыток в среднем копм угадывает рандом число)_

    Args:
        random_predict (_type_):(ф-я угадывания)_description_

    Returns:
        int: _description_(ср. к-во попыток)
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимомти (Метод random.seed() задает начальные условия для генератора случайных чисел)
    random_array= np.random.randint(1, 101, size=(1000)) #загадали список чисел.
    #последнее это сколько раз комп должен отгадать число. т.е. 1000 отгадываний
    for number in random_array:
        count_ls.append(random_predict(number)) #Добавляем в словарь количество попыток для вычисления числа из random_array
    score = int(np.mean(count_ls)) #np.mean всегда вычисляет среднее арифметическое.
    print(f"Ваш копм в среднем тратит {score} попыток на решение")
#RUN
score_game(random_predict)