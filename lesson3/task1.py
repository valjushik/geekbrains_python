import random
n = int(input("Введите длину последовательности: "))
numbers = [random.randint(1, 9) for i in range(n)]
print("Последовательность:", numbers)
sum = 0
i = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        sum = sum + numbers[i]
    else:
        i = i + 1

print("Сумма: ", sum)
