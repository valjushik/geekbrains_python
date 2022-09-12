import random

n = int(input("Введите число: "))
numbers = [i for i in range(1, n + 1)]

print(numbers)

for i in range(len(numbers) - 1):
    j = random.randint(0, len(numbers) - 1)
    numbers[i], numbers[j] = numbers[j], numbers[i]
    # t = numbers[i]
    # numbers[i] = numbers[j]
    # numbers[j] = t

print(numbers)
