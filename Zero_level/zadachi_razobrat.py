# Задача 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# # Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # мое решение
# for number in a:
#     if number <5:
#         print(f"числа меньше 5: {number}")
#
# print([number for number in a if number < 5]) # вот это прикольное решение  списковое включение:
#
# b = (1, 3, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89,100)
# print([number for number in b if number < 5]) # работат и для кортежей

result = [number for number in a if number <20]
print (result)


#Решение из учебника
# for elem in a:
#     if elem < 5:
#         print(elem)
# Также можно воспользоваться функцией filter, которая фильтрует элементы согласно заданному условию:
#
# print(list(filter(lambda elem: elem < 5, a)))
# И, вероятно, наиболее предпочтительный вариант решения этой задачи — списковое включение:
#
# # print([elem for elem in a if elem < 5])
# person = {
#
#     'name':'Victor',
#     'surname':'Vampire',
#     'age': 300,
#     'Location':'Hotel Transilvania',
#     'Любимое блюдо': ['кровь', 'девственицы', 'карбонара' ],
#     'Машина': 'Porsche',
#     'Hobby':'Кусать девок за сиськи',
# }
#
# print([key for key in person.items()])

# Задача 2
# Даны списки:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = a+b
print(c)  #тут я тупо сложил списки а надо было сделать не так  сделать один список в котором бы встречались значения
result = [number for number in a if number in b] # отличное решение которое можно прочитать так
# резулттиат числа для числа в а если число есть в б а потом принтим результат
# можно было сразу распринтить но тут был вариант который  придумал ранее
print (result)


# Вариант решения
# Можем воспользоваться функцией filter:
#
# result = list(filter(lambda elem: elem in b, a))
# Или списковым включением:
#
# result = [elem for elem in a if elem in b]



# Три словаря с цифрами сливаем в один
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

newSlovar ={} # создаем новый дикт
for sborka_slovarey in (dict_a,dict_b,dict_c): # с помошбю фора делаем пременную собирающщую
    # словарь Newsloavr и переменную счетчик sborka_slovarey и запускаем сборку

    newSlovar.update(sborka_slovarey)
print(newSlovar)


# Задача 5
# Найдите три ключа с самыми высокими значениями в
# словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

#Вот тут важно, я хотел колхозить какой то велосипед с ифами сравнивая между собой все подряд
# а в пайтоне кончено же есть встроенный сортировщик для таких как я

# итак берем словарь и применяем к нему sorted
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# resultat = sorted(my_dict.values())
# print(resultat)   # это просто сортировка а вот найти три ключа с самыми высокими значениями
#
# resultat = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(resultat)
# resultat = sorted(my_dict, val=my_dict.get, reverse=True)[:3]
# print(resultat)



liset_ot_baldy = [1,2,3, 27, 64, 0, ]

print(sorted(liset_ot_baldy))

liset_ot_baldy = ['a','b','c', 'a', 'e',' f' ]
print(sorted(liset_ot_baldy))
