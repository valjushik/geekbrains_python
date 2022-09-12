n = int(input("Введите число: "))
numbers = [i for i in range(-n, n + 1)]

print(numbers)
a = int(input("Введите A: "))
b = int(input("Введите B: "))

print(numbers[a-1] * numbers[b-1])
