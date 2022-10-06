n = int(input("Введите число: "))
b = ''
if n == 0:
    b = '00'
else:
    while n > 0:
        b = str(n % 2) + b
        n = int(n / 2)

print("Двоичное число: ", b)
