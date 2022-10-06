import math
import random
n = int(input("Введите длину последовательности: "))
numbers = [random.randint(1, 9) for i in range(n)]
print("Последовательность:", numbers)
i = 0
numbers2 = []
for i in range(math.ceil(n / 2)):
    numbers2.append(numbers[i] * numbers[n-i - 1])
print("Произведение: ", numbers2)
