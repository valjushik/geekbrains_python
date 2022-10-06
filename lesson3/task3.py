import math
import random

n = int(input("Введите длину последовательности: "))
numbers = [round(random.uniform(1, 9), 2) for _ in range(n)]
print("Последовательность:", numbers)
max = numbers[0]
min = numbers[0]
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        if numbers[i] > max:
            max = numbers[i]
        if numbers[i + 1] < min:
            min = numbers[i + 1]
    if numbers[i] < min:
        min = numbers[i]
    if numbers[i + 1] > max:
        max = numbers[i + 1]
print("max: ", max)
print("min: ", min)
print("Разница: ", round((max - min), 2))
