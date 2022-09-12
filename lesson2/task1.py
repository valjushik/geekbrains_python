n = input("Введите число: ")
s = 0

for i in n:
    if i.isdigit():
        s += int(i)
print("Сумма:", s)
