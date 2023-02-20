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
data_type.append(enter_type)
red_data_type=str(data_type).replace(';', ' ').split()
print(red_data_type)        

data_list=[]
while True:
    data_in_column=input("Введите данные: для первой колонки, затем для второй и тд. Используйте ранее выбранный вами разделитель: ")
    data_list.append(data_in_column)    
    if data_in_column == 'TRANSMISSION STOPPED':
        break #брык!
data_list.pop()  
print(data_list)


list_of_data=[]
for elem in data_list:
    el_str=str(elem).replace(';', ' ').split()
    list_of_data.append(el_str)
    if len(red_name_columns) != len (el_str):
        print("INVALID ELEMENTS NUMBER")
    
#если количество элементов в строке не соответствует заявленному ранее, печатать сообщение 
#  'INVALID ELEMENTS NUMBER' и начинать следующий ввод — 1 балл;
    

list_of_columns = list(zip(*list_of_data))
final_dict = dict(zip(red_name_columns, list_of_data))
print(final_dict)
        

