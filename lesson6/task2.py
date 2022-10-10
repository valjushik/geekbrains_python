#ДЗ 3. Задание 1
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Было

# import random
# n = int(input("Введите длину последовательности: "))
# numbers = [random.randint(1, 9) for i in range(n)]
# print("Последовательность:", numbers)
# sum = 0
# i = 0
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         sum = sum + numbers[i]
#     else:
#         i = i + 1
#
# print("Сумма: ", sum)



#Стало
import random
n = int(input("Введите длину последовательности: "))
numbers = [random.randint(1, 9) for i in range(n)]
print("Последовательность:", numbers)
filtered = [number for index, number in enumerate(numbers) if (index + 1) % 2 == 0]
print("Сумма: ", sum(filtered))
