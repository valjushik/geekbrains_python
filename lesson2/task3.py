n = int(input("Введите число: "))
a = [(1 + 1/i)**i for i in range(1, n + 1)]

print(a)

s = 0

for n in a:
    s += n

print(round(s, 3))
