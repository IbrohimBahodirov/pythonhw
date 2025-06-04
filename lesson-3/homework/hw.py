#--task1
fruit=input("5 meva kiriting: ").split()
print(fruit[2])

#-task2
lst1=input("1 chi listni kiriting: ").split()
lst2=input("2 chi listni kiriting: ").split()
lst3=lst1+lst2
print(lst3)

#--task3
numbers=[0,1,2,3,4,5,6,7,8,9,10]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

new_list = [first, middle, last]
print(new_list)

# --task4
films=['Inception','The Godfather ','Interstellar','The Shawshank Redemption','Joker ']
films=tuple(films)

#--task5
lst=["New York", "London", "Tokyo", "Paris", "Dubai"]
if 'Paris' in lst:
    print('Paris')
else:
    print('No Paris')

#--task6
import copy

lst=[0,1,2,3,4,5,6,7,8,9,10]
lst2=copy.deepcopy(lst)
print(lst2)

#--task7
numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

#--task8
tpl=(1,2,3,4,5,6,7,8,9,10)
print(tpl[2:7:2])

#--task9
colors = ["blue","sky blue","yellow", "red" , "aqua blue", "azure","purple"]
count = sum("blue" in i for i in colors)
print(count)

#--task10
animals = [
    "lion",
    "tiger",
    "elephant",
    "white lion",
    "giraffe",
    "zebra",
    "lion cub",
    "monkey",
    "rhino",
    "cheetah"
]
count = sum("lion" in i for i in animals)
print(count)


#--task11
fruits = ("apple", "banana", "orange", "grape")
numbers = (10, 20, 30, 40, 50)

fruits=list(fruits)
numbers=list(numbers)
lst3=fruits+numbers
lst3=tuple(lst3)
print(lst3)

#--task12
fruits = ["apple", "banana", "orange", "grape"]
numbers = (10, 20, 30, 40, 50)
print(f"length of list {len(fruits)}")
print(f"length of tuple {len(numbers)}")

#--task13
numbers = (10, 20, 30, 40, 50)
numbers=list(numbers)
print(numbers)
print(type(numbers))

#--task14
numbers = (10, 20, 30, 40, 50)
print(f"Max element {max(numbers)}")
print(f"Min element {min(numbers)}")

#--task15
fruits = ("apple", "banana", "orange", "grape")
fruits=list(fruits)
fruits.reverse()
print(fruits)
