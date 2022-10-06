print("RLE алгоритм: модуль сжатия данных:\n")
with open('decoded.txt', 'r') as data:
    my_text = data.read()

print(my_text)

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
print(str_code)

with open('output2.txt', 'w') as out:
    out.write(str_code)

####################################
print("\nRLE алгоритм: модуль восстановления данных:\n")

with open('encoded.txt', 'r') as data:
    my_text2 = data.read()
print(my_text2)

def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print(str_decode)

with open('output3.txt', 'w') as out:
    out.write(str_decode)
