#---task1

import math
class Doira:
    def __init__(self, radius):
        self.radius = radius

    def yuzi(self):
        return math.pi * self.radius ** 2

    def perimetri(self):
        return 2 * math.pi * self.radius

r = float(input("Doira radiusini kiriting: "))
doira = Doira(r)

print(f"Doiraning yuzi: {doira.yuzi():.2f}")
print(f"Doiraning perimetri: {doira.perimetri():.2f}")



#---task2

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date

    def age(self):
        from datetime import datetime
        today = datetime.today()
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

name=input("Ismingizni kiriting: ")
country=input("Yashash mamlakatingizni kiriting: ") 
birth_date=input("Tug'ilgan sanangizni YYYY-MM-DD formatida kiriting: ")
person = Person(name, country, birth_date)

print(f"Ism: {person.name}")
print(f"Mamlakat: {person.country}")    
print(f"Tug'ilgan sana: {person.birth_date}")
print(f"Yoshi: {person.age()}")

#---task3

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Division by zero is not allowed."
        return a / b
    def power(self, a, b):
        return a ** b
    def modulus(self, a, b):    
        return a % b
    def floor_division(self, a, b):
        return a // b
    def square_root(self, a):
        if a < 0:
            return "Square root of negative number is not allowed."
        return a ** 0.5
    def absolute(self, a,b):
        return abs(a), abs(b)
   
a= float(input("Birinchi sonni kiriting: "))
b= float(input("Ikkinchi sonni kiriting: "))
calc = Calculator()

print(f"{a} + {b} = {calc.add(a, b)}")
print(f"{a} - {b} = {calc.subtract(a, b)}") 
print(f"{a} * {b} = {calc.multiply(a, b)}")
print(f"{a} / {b} = {calc.divide(a, b)}")
print(f"{a} ** {b} = {calc.power(a, b)}")
print(f"{a} % {b} = {calc.modulus(a, b)}")
print(f"{a} // {b} = {calc.floor_division(a, b)}")
print(f"√{a} = {calc.square_root(a)}")
print(f"√{b} = {calc.square_root(b)}")
abs_a, abs_b = calc.absolute(a, b)

#--task4
import math

class Forma:
    def yuzi(self):
        raise NotImplementedError("Bu metodni subclassda aniqlang.")

    def perimetri(self):
        raise NotImplementedError("Bu metodni subclassda aniqlang.")

class Doira(Forma):
    def __init__(self, radius):
        self.radius = radius

    def yuzi(self):
        return math.pi * self.radius ** 2

    def perimetri(self):
        return 2 * math.pi * self.radius

class Kvadrat(Forma):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuzi(self):
        return self.tomon ** 2

    def perimetri(self):
        return 4 * self.tomon
    
class Uchburchak(Forma):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetri(self):
        return self.a + self.b + self.c

    def yuzi(self):
        p = self.perimetri() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  

doira = Doira(int(input("Doira radiusini kiriting: ")))
kvadrat = Kvadrat(int(input("Kvadrat tomonini kiriting: ")))
uch = Uchburchak(
    int(input("Uchburchakning birinchi tomonini kiriting: ")),
    int(input("Uchburchakning ikkinchi tomonini kiriting: ")),
    int(input("Uchburchakning uchinchi tomonini kiriting: "))
)

print("Doira: Yuzi =", round(doira.yuzi(), 2), " Perimetri =", round(doira.perimetri(), 2))
print("Kvadrat: Yuzi =", kvadrat.yuzi(), " Perimetri =", kvadrat.perimetri())
print("Uchburchak: Yuzi =", round(uch.yuzi(), 2), " Perimetri =", uch.perimetri())


#---task5
class Node:
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.chap = None
        self.ong = None

class Daraxt:
    def __init__(self):
        self.koreni = None

    def qoshish(self, qiymat):
        if self.koreni is None:
            self.koreni = Node(qiymat)
        else:
            self._qosh(self.koreni, qiymat)

    def _qosh(self, tugun, qiymat):
        if qiymat < tugun.qiymat:
            if tugun.chap is None:
                tugun.chap = Node(qiymat)
            else:
                self._qosh(tugun.chap, qiymat)
        else:
            if tugun.ong is None:
                tugun.ong = Node(qiymat)
            else:
                self._qosh(tugun.ong, qiymat)

    def qidirish(self, qiymat):
        return self._qidir(self.koreni, qiymat)

    def _qidir(self, tugun, qiymat):
        if tugun is None:
            return False
        if tugun.qiymat == qiymat:
            return True
        if qiymat < tugun.qiymat:
            return self._qidir(tugun.chap, qiymat)
        else:
            return self._qidir(tugun.ong, qiymat)

d = Daraxt()
d.qoshish(10)

print(d.qidirish(5))   
print(d.qidirish(20)) 

#---task6
class Stek:
    def __init__(self):
        self.ichida = []

    def qoshish(self, narsa):
        self.ichida.append(narsa)

    def olish(self):
        if self.ichida:
            return self.ichida.pop()
        else:
            return "Stek bo‘sh"
s = Stek()
s.qoshish(10)

print(s.olish()) 

#---task7
class Node:
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.keyingi = None

class Royxat:
    def __init__(self):
        self.boshi = None

    def qoshish(self, qiymat):
        yangi = Node(qiymat)
        yangi.keyingi = self.boshi
        self.boshi = yangi

    def ochirish(self, qiymat):
        t = self.boshi
        oldingi = None
        while t and t.qiymat != qiymat:
            oldingi = t
            t = t.keyingi
        if not t:
            return
        if oldingi:
            oldingi.keyingi = t.keyingi
        else:
            self.boshi = t.keyingi

    def chiqarish(self):
        t = self.boshi
        while t:
            print(t.qiymat, end=" -> ")
            t = t.keyingi
        print("None")
r = Royxat()
r.qoshish(10)

r.chiqarish()    



#---task8

class Savatcha:
    def __init__(self):
        self.tovarlar = {}

    def qoshish(self, nomi, narxi, soni=1):
        if nomi in self.tovarlar:
            self.tovarlar[nomi][1] += soni
        else:
            self.tovarlar[nomi] = [narxi, soni]

    def ochirish(self, nomi):
        if nomi in self.tovarlar:
            del self.tovarlar[nomi]

    def umumiy_narx(self):
        summa = 0
        for narx, son in self.tovarlar.values():
            summa += narx * son
        return summa
s = Savatcha()
s.qoshish("Olma", 2000, 2)
s.qoshish("Non", 3000)
print(s.umumiy_narx())  

s.ochirish("Olma")
print(s.umumiy_narx())

#---task9
class Stek:
    def __init__(self):
        self.malumot = []

    def qoshish(self, narsa):
        self.malumot.append(narsa)

    def olish(self):
        if self.malumot:
            return self.malumot.pop()
        return "Bo‘sh"

    def korsat(self):
        print("Stek:", self.malumot)
s = Stek()
s.qoshish("kitob")

s.korsat()         
s.olish()          
s.korsat()         

#---task10
class Navbat:
    def __init__(self):
        self.navbat = []

    def qoshish(self, narsa):
        self.navbat.append(narsa)

    def olish(self):
        if self.navbat:
            return self.navbat.pop(0)
        return "Bo‘sh"
n = Navbat()
n.qoshish("Ali")
n.qoshish("Vali")
print(n.olish())   
print(n.olish())   
print(n.olish())   

#---task11
class Bank:
    def __init__(self, ism):
        self.ism = ism
        self.balans = 0

    def depozit(self, summa):
        self.balans += summa
        print("Yangi balans:", self.balans)

    def yechish(self, summa):
        if summa <= self.balans:
            self.balans -= summa
            print("Yechildi:", summa)
        else:
            print("Yetarli mablag' yo'q.")

    def korsat_balans(self):
        print("Balans:", self.balans)

b = Bank("Ibrohim")
b.depozit(10000)
b.yechish(3000)         
b.korsat_balans()      

b.yechish(8000)        
