fruits=[мандарин, апельсин, манго, банан, кокос, яблоко, пасатижи]
new_list=[x for x in fruits if x!="Яблоко"]
#Будет в new_list все, кроме яблока.


en_option= translit(un_enter3, language_code='ru', reversed=True)

for_value3 = un_enter3.split(sep=',') #Разделяем строку по раделителю ","
value_option=en_option.split(sep=',')
for_keys3 = un_enter2.split(sep=',')

list_of_value3 = []
for object3 in for_value3:          #Создаю цикл для "очистки значений" от первого пробела
  clean_object3 = object3.strip()
  list_of_value3.append(clean_object3)
  
list_option_value3 = []
for option in value_option:          #Создаю цикл для "очистки значений" от первого пробела
  option_object3 = option.strip()
  list_option_value3.append(clean_object3)
  
result3 = []
for word3 in list_of_value3:
  subwords3 = word3.split() #Разделяю элементы на отдельные значения (sep=' ')
  subres3 = []
  for subword3 in subwords3: 
    subres3.append(subword3[0:4]) #В этих значениях ограничиваю длину до 4-х символов
  word3 = '_'.join(subres3) #Соединяю получившееся через "_"
  result3.append(word3) 
  
option_result = []
for option_word in list_option_value3:
  subwords4 = option_word.split() #Разделяю элементы на отдельные значения (sep=' ')
  subres4 = []
  for subword4 in subwords4: 
    subres4.append(subword4[0:4]) #В этих значениях ограничиваю длину до 4-х символов
  option_word = '_'.join(subres4) #Соединяю получившееся через "_"
  option_result.append(option_word) 

list_of_keys3 = []
for key3 in for_keys3:          #Создаю цикл для "очистки значений" от первого пробела
  clean_key3 = key3.strip()
  list_of_keys3.append(clean_key3)   

general_key = list_of_keys3[0]
first_value = list_of_keys3[1::]   
second_value = result3[1::]
option_value= option_result[1::] 
final_dict = dict(zip(first_value, second_value))
final_dict2 = dict(zip(first_value, option_value)) 




for transliteral in first_liter:
  if ord(first_liter) >= min_ord and ord(first_liter) <=max_ord:
    for key, value in final_dict.items():
      print (f'CASE WHEN {general_key} = {key} THEN 1 ELSE 0 END AS {value}')
    else:
      for key2, value2 in final_dict2.items():
        print (f'CASE WHEN {general_key} = {key2} THEN 0 ELSE 1 END AS {value2}')
        
print(un_enter3)



for transliteral in first_liter:
  if 97 <= first_liter >= 122:
    for key, value in final_dict.items():
      print (f'CASE WHEN {a3} = {key} THEN 1 ELSE 0 END AS {value}')
    else:
      final_dict2= translit(final_dict, language_code='ru', reversed=True)
      for key, value in final_dict2.items():
        print (f'CASE WHEN {a3} = {key} THEN 0 ELSE 1 END AS {value}')


def transliteral(final_dict):
  for liter in a3:
    if 97 < ord(liter[0]) > 122:
      for key, value in final_dict.items():
        return print (f'CASE WHEN {a3} = {key} THEN 1 ELSE 0 END AS {value}')
    else:
      final_dict2= translit(final_dict, language_code='ru', reversed=True)
      for key, value in final_dict2.items():
        return print (f'CASE WHEN {a3} = {key} THEN 1 ELSE 0 END AS {value}')

for key, value in final_dict.items():
  print (f'CASE WHEN {a} = {key} THEN 1 ELSE 0 END AS {value}') 

for posicion in experimental_dict:
  print (f'CASE WHEN {a} = {posicion.keys()} THEN 1 ELSE 0 END AS {posicion.values()}')  

from transliterate import translit
def translit_function(unicod_number):
  for unicod_number in a:
    if 97 < ord(unicod_number[0]) > 122:
      new_d= translit(d, language_code='ru', reversed=True)
      return d==new_d
    else:
      pass

set_res = set(b)
set_res2=set(d)
list_res = (list(set_res))
list_res2=(list(set_res2)) 
len_set = len(list_res)

final_dict = dict(zip(b, d))
print(final_dict)