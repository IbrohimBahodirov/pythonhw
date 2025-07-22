
import numpy as np

# task1
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)

print("Одномерный массив NumPy:", arr)
# task2
arr = np.arange(2, 11).reshape(3, 3)
print(arr)

vec = np.zeros(10)
print("До обновления:", vec)
# task3
vec[6] = 11
print("После обновления:", vec)
# task4
arr = np.arange(12, 38)
print(arr)
# task5
arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)
print(float_arr)
# task6
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32

print("Значения в градусах Цельсия:", celsius)
print("Значения в градусах Фаренгейта:", fahrenheit)
# task7
arr = np.array([10, 20, 30])
new_values = [40, 50, 60, 70, 80, 90]
arr = np.append(arr, new_values)
print("После добавления:", arr)
# task8
arr = np.random.randint(1, 100, size=10)

print("Массив:", arr)
print("Среднее:", np.mean(arr))
print("Медиана:", np.median(arr))
print("Станд. отклонение:", np.std(arr))
# task9
arr = np.random.rand(10, 10)

print("Минимум:", arr.min())
print("Максимум:", arr.max())
# task10
arr = np.random.rand(3, 3, 3)
print(arr)
