#ДЗ 4. Задание 2
#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#Было
# import random
# n = int(input("Введите длину последовательности: "))
# numbers = [random.randint(1, n) for i in range(n)]
# print("Последовательность:", numbers)
#
# unique = []
# for i in range(len(numbers)):
#     isUnique = True
#     for j in range(len(numbers)):
#         if i != j and numbers[i] == numbers[j]:
#             isUnique = False
#
#     if isUnique:
#         unique.append(numbers[i])
#
# print("Уникальные:", unique)



#Стало
import random
n = int(input("Введите длину последовательности: "))
numbers = [random.randint(1, n) for i in range(n)]
print("Последовательность:", numbers)
filtered = filter(lambda x: 1 == len(list(filter(lambda y: y == x, numbers))), numbers)
print("Уникальные:", list(filtered))
