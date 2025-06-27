#--task1
txt = input()
result = ""
i = 0
count = 0
while i < len(txt):
    result += txt[i]
    count += 1
    if count == 3:
        if txt[i] not in "aeiou" and (i + 1 >= len(txt) or txt[i + 1] != "_"):
            result += "_"
        count = 0
    i += 1
if result.endswith("_"):
    result = result[:-1]
print(result)
#--task2
n = int(input())
for i in range(n):
    print(i * i)


#--task3
i = 1
while i <= 10:
    print(i)
    i += 1
#--task4
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#--task5
n = int(input("Enter number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum is:", sum)
#--task6
n = int(input())
for i in range(1, 11):
    print(n * i)
#--task7
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)
#--task8
num = int(input())
count = 0
while num != 0:
    num //= 10
    count += 1
print(count)
#--task9
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
#--task10
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
#--task11
for i in range(-10, 0):
    print(i)
#--task12
for i in range(5):
    print(i)
print("Done!")
#--task13
for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#--task14
a = 0
b = 1
print(a, b, end=" ")
for _ in range(8):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
#--task15
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)
#--task16
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result = []

for i in list1:
    if list2.count(i) == 0:
        result.append(i)
    else:
        list2.remove(i)

result += list2
print(result)
