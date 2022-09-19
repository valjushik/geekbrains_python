n = int(input("Введите число: "))
i = 2
delit = []
while i * i <= n:
    while n % i == 0:
        delit.append(i)
        n = int(n / i)
    i = i + 1
if n > 1:
    delit.append(n)
print("Делители:", delit)
