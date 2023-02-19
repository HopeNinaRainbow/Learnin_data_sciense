while True:
    sequence =input("Выберите разделитель (запятая, точка-с-запятой или пробел) и введите в поле для ответа: ")
    if ' ' in sequence:
        delimiter= ' '
    elif ',' in sequence:
        delimiter= ','
    elif ';' in sequence:
        delimiter = ';'
        break
    else:
        print('Разделителем может быть только...бла-бла')
print(delimiter) #Эта строка только для того, чтобы проверить, что в в переменной реально храниться разделитель.

while True:
    columns=input("Введите названия колонок для вашей таблицы, разделяя слова выбранным ранее разделителем: ")
    name_columns=[]
    if delimiter in columns:
        name_columns.append(columns)
        break
    else:
        print("Используйте разделитель указанный вами ранее")
red_name_columns=str(name_columns).split(delimiter)
print(red_name_columns) #Проверка работы кода
        
enter_type=input('через разделитель введите тип данных для каждой колонки: числовые данные-float, int; текст-str; булевые-bool: ')
data_type=[] 
data_type.append(str(enter_type))
print(data_type)

data_list=[]
while True:
    data_in_column=input("Введите данные: для первой колонки, затем для второй и тд. Используйте ранее выбранный вами разделитель: ")
    data_list.append(data_in_column)    
    if data_in_column == 'TRANSMISSION STOPPED':
        break #брык!
data_list.pop()  
print(data_list)

list_of_rows = big_string.split('\n')


        
        

