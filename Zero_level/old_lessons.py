# number_list = [1,2,3,4,5,6,7,8,9,10] # просто вывести все цифры
# for number in number_list:
#     print (number)
#     print ("hola")
#

# Четное не четное с помощью цикала фор
# number_list = [1,2,3,4,5,6,7,8,9,10]
# for number in number_list:
#     if number %2 ==0: # если делится  (%) на два без остатка (==0) тру нулю  % оператор модула
#         print (number, "Четное")
#     else:
#         print(number, "НЕ Четное")


# еще один вариант типа ссчетчика с добавлением + число  (list_numbers_summ = list_numbers_summ+number)
# number_list = [1,2,3,4,5,6,7,8,9,10]
# list_numbers_summ =0
# for number in number_list:
#     list_numbers_summ = list_numbers_summ+number
#     print (list_numbers_summ)
#



# greeting ='Hello python'
# for letter in greeting:
#     print(letter)
#Выведеие в цикле букв из строк
#greeting = 'Hello python'
# for letter in greeting:
#     if letter == 'o':
#         print(letter)


# greeting = 'Hello python'
# for letter in greeting:
#     if letter != 'o':
#         print(letter)

#а можно цикл вообще без переменной исползовать сразу строку хуячить
# for letter in 'Hello python':
#     if letter != 'o':
#         print(letter)

#Следи за руками  напринталось выражение 'One more letter' стколько раз сколько букв в Hello python'
# for letter in 'Hello python':
#          print('One more letter')
#
#
# tuple_list = [("a", "b"), ("c", "d"), ('e', 'f') ]
# for element in tuple_list:
#     print(element)
#
# for letter_1, letter_2 in tuple_list:
#     print(letter_1)
#     print(letter_2)

# Вывод из тупла, вообще непонятно какпайтон понимает какой элемент выводить
# tuple_list = [("a", "b",1 ), ("c", "d", 4), ('e', 'f', 5)]
# for letter_1, letter_2, number in tuple_list:
#     print(letter_1,letter_2,number)


#работа с диктами
# если просто пишем в диект обращение к елементу for element in dictionary:
#     print(element) то он отдает  только ключи, чтобы получить  все значения и ключ и значение надо добавить
#     items  это метод дикта выгдядит так dictionary.items смотри ниже
# dictionary = {'key1': "value1", 'key2': "value2", 'key3': "value3" }
# for element in dictionary:
#     print(element)
# for element in dictionary.items():
#     print(element)
# for element in dictionary.keys():
#     print(element)
# for element in dictionary.values():
#     print(element)

for x in range (11):
    print (x)
for _ in range (5):
    print ("Похую что выводить ")
