str1 = input("Введите строку: ")
str2 = input("Введите строку: ")

c = 0

for i in range(len(str1)):
    if str1[i:i+len(str2)] == str2:
        c += 1

print(c)
