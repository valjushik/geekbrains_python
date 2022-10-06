#!/usr/bin/env python
# -*- coding: windows-1251 -*-

with open('input1.txt', 'r') as data:
    my_text = data.read()
print(my_text)


def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)


my_text = del_some_words(my_text)
print(my_text)

with open('output1.txt', 'w') as out:
    out.write(my_text)
