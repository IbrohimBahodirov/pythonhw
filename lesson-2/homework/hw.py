# Домашнее задание Упражнения
# 1. Калькулятор возраста
# Напишите программу на Python, которая будет запрашивать имя и год рождения пользователя,
# а затем вычислять и отображать его возраст.

# 2. Извлечение названий автомобилей
# Извлеките названия автомобилей из следующего текста:
# txt = 'LMaasleitbtui'

# 3. Извлечение названий автомобилей
# Извлеките названия автомобилей из следующего текста:
# txt = 'MsaatmiazD'

# 4. Извлечение жилой зоны
# Извлеките область проживания из следующего текста:
# txt = "I'am John. I am from London"

# 5. Обратная строка
# Напишите программу на Python, которая принимает введенную пользователем строку и выводит ее в обратном порядке.

# 6. Подсчитайте гласные
# Напишите программу на Python, которая подсчитывает количество гласных в заданной строке.

# 7. Найдите максимальное значение
# Напишите программу на Python, которая принимает в качестве входных данных список чисел
# и выводит максимальное значение.

# 8. Проверьте Палиндром
# Напишите программу на Python, которая проверяет, является ли заданное слово палиндромом (читается одинаково слева направо и справа налево).

# 9. Извлечение домена электронной почты
# Напишите программу на Python, которая извлекает и выводит домен из адреса электронной почты,
# предоставленного пользователем.

# 10. Сгенерируйте случайный пароль
# Напишите программу на Python для генерации случайного пароля,
# содержащего буквы, цифры и специальные символы.

#--task1
ism=input("Ismingizni kiriting: ")
yil=int(input("Tug'ilgan yilingizni kiriting: "))
print(f"Salom {ism} siz {2025-yil} yoshdasiz")

# #---task2
txt = 'LMaasleitbtui'
car1 = txt[::2]   
car2 = txt[1::2]  

print("Birinchi avtomobil:", car1)
print("Ikkinchi avtomobil:", car2)

# #--task3
txt = 'MsaatmiazD'
car1=txt[::2]
car2=txt[-1::-2]
print(car1)
print(car2)

# #---task4
txt = "I'am John. I am from London"
print(txt[txt.find('L')::])

#---task5
str=input("Satr kiriting: ")
print(str[-1::-1])

# --task6
str=input("Satr kiriting: ")
vovels = 'auioey'
cnt=0
for i in str:
    if i.lower() in vovels:
        cnt = cnt + 1
print(cnt)

# ---task7
lst=list(input("Sonlarni kiriting: "))
print(max(lst))

# --task8
str=input("Satr kiriting: ")


if str.lower()==str[-1::-1].lower():
    print("Satr polindrom ")
else :
    print("Satr polindrom emas")

# ---task9
str=input("Elektron pochtangizni  kiriting: ")
lst=str.split('@')
print(''.join(lst))

#--task10
import random
import string

xarflar = string.ascii_letters       
raqamlar = string.digits              
simvollar = string.punctuation     

password = [random.choice(xarflar),random.choice(raqamlar),random.choice(simvollar)]

all_chars = xarflar+raqamlar+simvollar
password += random.choices(all_chars)

random.shuffle(password)

print("Tasodifiy parol :", (''.join(password)))
