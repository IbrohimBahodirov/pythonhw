#--task1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Misollar
print(is_prime(4))   # False
print(is_prime(7))   # True


#--task2
def digit_sum(k):
    sum = 0
    while k > 0:
        sum += k % 10
        k //= 10
    return sum

# Misollar
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7


#-- task3
def print_powers_of_two(N):
    power = 1
    while power * 2 <= N:
        power *= 2
        print(power, end=" ")

# Misol
print_powers_of_two(10)  # 2 4 8
