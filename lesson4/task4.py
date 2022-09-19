import random

k = int(input("Введите k: "))
numbers = [random.randint(0, 100) for i in range(k + 1)]
stroka = ""
print("Коэффициенты:", numbers)
for j in range(len(numbers)):
    if numbers[j] > 0:
        if len(stroka) > 0:
            stroka += " + "
        if numbers[j] > 1 or k == 0:
            stroka += str(numbers[j])
        if k > 0:
            stroka += "x"
        if k > 1:
            stroka += "^" + str(k)
    k = k-1

stroka += " = 0"
print("Уравнение:", stroka)
