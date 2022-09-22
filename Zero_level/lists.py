names =["Белла", "Снежанна", "Виолетта", "Изабэлла"]

numbers =[3,1, 3.4, 'Stringa']

print(numbers)
numbers =[3,1, 3.4, 'Stringa', ['xyi', 30, 'cm']]

print(numbers)

print(names[0:4])

for name in names:
    print(name)


names.append( 'Бралочка')
names.append( 'Давалочка')

print(names)

names.pop() #метод поп тупо удаляет последний элемент без передачи аргуемнтов

print(names)


nomer = names.index('Бралочка') # узнать номер индекса по значению в списке

print (nomer)

print ('x'*30)

print(len(names))

listint =[1,2,3,4,8,0,4,6]
listint.sort()
print(listint)

listint[0]= 'Xyi'
print(listint)

names.append('Артемона')
names.sort()
print(names)
names.reverse()
print(names)
