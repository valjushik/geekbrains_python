n = int(input("Введите число: "))
s = 1
i = int(1)
a = [1]
#for i in n:
for i in range(1, n):
    s *= i
    a.append(a[i - 1] * (i + 1))
#print("Сумма:", s)

print(a)
