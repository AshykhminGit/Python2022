


import datetime
print(datetime.date.today())

name = str(input("Введите имя пожалуйста: "))
print(name)
age =int(input("Введите возраст: "))
today = int(input("введите какой сейчас год"))
year_of_birth = today-age
print(f"Вы {year_of_birth} года рождения")

print(f"{year_of_birth} был замечательный")

#проверка вохраста пользователя
if age <18:
    print ("Вы не можете войти, вам меньше 18 лет")
else:
    print ("Заходите к нам:")

    zp_sechina  =int(input(f"Введите за Сечина в год"))
    zp_sechina = zp_sechina//12
    print(f" зп Сечина в месяц {zp_sechina}")


# ип1  15 %  физ лицо 13 %  остально 6 %
business_type = str(input("Ввведите вид деятельности"))

income = int(input('введите размер дохода'))

#прописываем условия для разныъ форматов 3налогообложения для бизнеса
if business_type == 'ип1':
    tax = income * 0.15
    net_income = income - tax
    print(f"  - {name}  чистый доход {business_type}: {net_income} рублей, а налог составит {tax} рублей")
elif business_type == 'фл':
    tax = income * 0.13
    net_income = income - tax
    print(f"  + {name} чистый доход {business_type}: {net_income} рублей, а налог составит {tax} рублей")
elif business_type == 'чп' or  business_type == 'ЧП':
    tax = income * 0.06
    net_income = income - tax
    print(f" {name.split()}   чистый доход {business_type}: {net_income} рублей, а налог составит {tax} рублей")
    if net_income >= zp_sechina:
        print(f"Да ты красавчик у тебя зарплата {net_income}, а у него всего то {zp_sechina}")
    else:
        print(f"Ну как то надо больше работать или воровать. У него офигеннаяв  {zp_sechina} рублей,"
              f" а  у тебя {net_income} ")

else:
    print(f"{name}, что то пошло не так")

