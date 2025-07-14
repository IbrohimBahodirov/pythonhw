# Домашнее задание:

# Упражнение 1: Поточная проверка простых чисел

# Напишите программу Python, которая проверяет, содержит ли заданный диапазон чисел простые числа.
#  Разделите диапазон между несколькими потоками, чтобы распараллелить процесс проверки на простоту.
#  Каждый поток должен отвечать за проверку подмножества диапазона, а основная программа должна выводить список найденных простых чисел.

# Упражнение 2: Поточная обработка файлов

# Напишите программу, которая читает большой текстовый файл, содержащий строки текста.
#  Реализуйте потоковое решение для подсчета вхождений каждого слова в файле.
#  Каждый поток должен обрабатывать часть файла, а основная программа должна отображать
#  сводку вхождений слов во всех потоках.


import threading


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)


def main():
    start_range = 1
    end_range = 1000
    num_threads = 4

    
    step = (end_range - start_range) // num_threads
    threads = []
    results = [[] for _ in range(num_threads)]  

    for i in range(num_threads):
        start = start_range + i * step
        
        end = end_range if i == num_threads - 1 else start + step
        thread = threading.Thread(target=check_primes, args=(start, end, results[i]))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join()

    
    all_primes = []
    for sublist in results:
        all_primes.extend(sublist)

    all_primes.sort()
    print("Topilfgan tub sonlar:")
    print(all_primes)

if __name__ == "__main__":
    main()


#--task2
import threading

def count_words(lines, result):
    words = {}
    for line in lines:
        for word in line.strip().lower().split():
            word = word.strip('.,!?":;()[]') 
            if word:
                words[word] = words.get(word, 0) + 1
    result.append(words)

def main():
    with open('file.txt', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    num_threads = 4
    chunk_size = len(all_lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = len(all_lines) if i == num_threads - 1 else (i + 1) * chunk_size
        part = all_lines[start:end]

        result = []
        thread = threading.Thread(target=count_words, args=(part, result))
        threads.append((thread, result))
        thread.start()


    total = {}

    for thread, result in threads:
        thread.join()
        for word, count in result[0].items():
            total[word] = total.get(word, 0) + count


    for word, count in sorted(total.items(), key=lambda x: -x[1])[:10]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
