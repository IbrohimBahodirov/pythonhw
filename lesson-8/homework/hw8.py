#--task1

try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    result = a / b
    print("Результат деления:", result)
except ZeroDivisionError:
    print("Xatolik: Nol ga bo'lish mumkin emas.")


#--task2

try:
    number = int(input("Iltimos, butun son kiriting: "))
    print("Siz kiritgan son:", number)
except ValueError:
    print("Xatolik: Butun son kiritilmadi!")


#--task3
filename = input("File nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        file = file.read()
        print("File da gi malumotlar:")
        print(file)
except FileNotFoundError:
    print(f"Xatolik: File '{filename}' topilmadi.")
      
#--task4

try:
    number1 = int(input("Iltimos, son kiriting: "))
    number2 = int(input("Iltimos, son kiriting: "))
    print(f"Siz kiritgan sonlar:", {number1}, {number2})
except ValueError:
    print("Xatolik: Son kiritilmadi!")

#--task5
try:
    with open("C:\\Users\\user\\Desktop\\PyHomework\\lesson8\\file.txt", "r") as fayl:
        print(fayl.read())
except PermissionError:
    print("Xatolik: Faylni ochish uchun ruxsat yo'q.")
#--task6
try:
    lst = [10, 20, 30]
    index = int(input("Indeks kiriting (0 dan 2 gacha): "))
    print("Qiymat:", lst[index])
except IndexError:
    print("Xatolik: Indeks ro'yxat chegarasidan tashqarida.")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting.")
#--task7
try:
    son = int(input("Iltimos, son kiriting: "))
    print("Siz kiritgan son:", son)
except KeyboardInterrupt:
    print("\nXatolik: Kiritish bekor qilindi foydalanuvchi tomonidan.")
except ValueError:
    print("Xatolik: Son kiriting.")
#--task8
try:
    a = float(input("Soni kiriting: "))
    b = float(input("Bo‘luvchini kiriting: "))
    natija = a / b
    print("Natija:", natija)
except ArithmeticError:
    print("Xatolik: Aritmetik xato yuz berdi.")
#--task9
try:
    with open("fayl.txt", encoding="utf-8") as fayl:
        print(fayl.read())
except UnicodeDecodeError:
    print("Xatolik: Kodlash (encoding) bilan bog'liq muammo yuz berdi.")
#--task10
try:
    royxat = [1, 2, 3]
    royxat.upper()  
except AttributeError:
    print("Xatolik: Bunday atribut yoki metod mavjud emas.")


#--task10
with open("matn.txt", "r", encoding="utf-8") as fayl:
    mazmun = fayl.read()
    print("Fayl mazmuni:")
    print(mazmun)


#--task11
n = int(input("Nechta qatordan boshlab o'qilsin: "))

with open("matn.txt", "r", encoding="utf-8") as fayl:
    for i in range(n):
        qator = fayl.readline()
        if not qator:
            break
        print(qator.strip())

#--task12
with open("matn.txt", "a", encoding="utf-8") as fayl:
    yangi_matn = input("Faylga qanday matn qo'shilsin? ")
    fayl.write(yangi_matn + "\n")

#--task13
with open("matn.txt", "r", encoding="utf-8") as fayl:
    print("Yangi fayl mazmuni:")
    print(fayl.read())

#--task14
n = int(input("Oxirdan nechta qatordan o'qilsin: "))

with open("matn.txt", "r", encoding="utf-8") as fayl:
    barcha_qatorlar = fayl.readlines()
    oxirgi_qatorlar = barcha_qatorlar[-n:]
    print("Oxirgi", n, "qator:")
    for qator in oxirgi_qatorlar:
        print(qator.strip())


#-- task15
with open("file.txt", "r", encoding="utf-8") as f:
    lines_list = f.readlines()
print("Qatorlar ro'yxatga saqlandi:", lines_list)
print("-" * 50)


#--task16
with open("file.txt", "r", encoding="utf-8") as f:
    text_var = f.read()
print("Fayl matni o'zgaruvchiga saqlandi:\n", text_var)
print("-" * 50)


# --task17
with open("file.txt", "r", encoding="utf-8") as f:
    lines_array = [line.strip() for line in f]
print("Qatorlar massivga saqlandi:", lines_array)
print("-" * 50)


# --task18
with open("file.txt", "r", encoding="utf-8") as f:
    words = f.read().replace(",", " ").split()
    max_len = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_len]
print("Eng uzun so'z(lar):", longest_words)
print("-" * 50)


# --task19
with open("file.txt", "r", encoding="utf-8") as f:
    num_lines = sum(1 for _ in f)
print("Qatorlar soni:", num_lines)
print("-" * 50)


# --task20
from collections import Counter
with open("file.txt", "r", encoding="utf-8") as f:
    words = f.read().replace(",", " ").split()
    word_freq = Counter(words)
print("So'z chastotasi:", word_freq)
print("-" * 50)


# --task21
import os
size = os.path.getsize("file.txt")
print("Fayl hajmi (baytda):", size)
print("-" * 50)


# --task22  
my_list = ["salom", "dunyo", "python"]
with open("list_output.txt", "w", encoding="utf-8") as f:
    for item in my_list:
        f.write(item + "\n")
print("Ro'yxat faylga yozildi.")
print("-" * 50)


# --task23
with open("file.txt", "r", encoding="utf-8") as source, open("file_copy.txt", "w", encoding="utf-8") as dest:
    dest.write(source.read())
print("Fayl nusxalandi.")
print("-" * 50)


# --task24
with open("file1.txt", "r", encoding="utf-8") as f1, open("file2.txt", "r", encoding="utf-8") as f2:
    combined = [a.strip() + " " + b.strip() for a, b in zip(f1, f2)]
with open("merged.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(combined))
print("Fayllar qatorlar bo‘yicha birlashtirildi.")
print("-" * 50)


#-- task25
import random
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    rand_line = random.choice(lines).strip()
print("Tasodifiy qator:", rand_line)
print("-" * 50)


#-- task25
f = open("file.txt", "r", encoding="utf-8")
f.close()
print("Fayl yopilgan:", f.closed)
print("-" * 50)


#-- task25
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
cleaned_lines = [line.strip() for line in lines]
print("Yangi qator belgisisiz:", cleaned_lines)
print("-" * 50)


#-- task25
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read().replace(",", " ").replace(".", " ")
    words = text.split()
print("So'zlar soni:", len(words))
print("-" * 50)


#-- task25
files = ["file1.txt", "file2.txt"]
chars = []
for fname in files:
    with open(fname, "r", encoding="utf-8") as f:
        chars.extend(list(f.read()))
print("Harflar ro'yxati:", chars)
print("-" * 50)


#-- task25
import string
for harf in string.ascii_uppercase:
    with open(f"{harf}.txt", "w", encoding="utf-8") as f:
        f.write(f"Bu {harf}.txt faylidir.\n")
print("A dan Z gacha fayllar yaratildi.")
print("-" * 50)


#-- task25
harf_soni = 5 
with open("alphabet.txt", "w", encoding="utf-8") as f:
    alfabe = string.ascii_uppercase
    for i in range(0, len(alfabe), harf_soni):
        f.write(alfabe[i:i+harf_soni] + "\n")
print("Har bir qatorda belgilangan harflar bilan fayl yaratildi.")
print("-" * 50)
