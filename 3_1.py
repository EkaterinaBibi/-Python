#A

n = int(input())
list_ = ['а', 'б', 'в']
for i in range(n):
    name = input()
    if name[0] not in list_:
        print('NO')
        break
else:
    print('YES')

#B

name = input()
for i in range(len(name)):
    print(name[i])

#C

len_ = int(input())
n = int(input())
for i in range(n):
    name = input()
    if len(name) > len_:
        print(name[:len_ - 3] + '...')
    else:
        print(name)

#D

while name := input():
    if name.endswith('@@@'):
        print('', end='')
    elif name[:2] == '##':
        print(name[2:])
    else:
        print(name)

#E

name = input()
if name == name[::-1]:
    print('YES')
else:
    print('NO')

#F

n = int(input())
count = 0
for i in range(n):
    name = input()
    count += name.count('зайка')
print(count)

#G

string = input()
lst = string.split()
print(int(lst[0]) + int(lst[1]))

#H

n = int(input())
for i in range(n):
    name = input()
    if 'зайка' in name:
        print(name.index('зайка') + 1)
    else:
        print('Заек нет =(')

#I

while name := input():
    if '#' in name:
        index = name.index('#')
        if index == 0:
            print('', end='')
        else:
            print(name[:index])
    else:
        print(name)

#J

ount = 0
text = ''
list_char = []
list_word = []
while (word := input()) != 'ФИНИШ':
    list_char += word.lower()
for char in list_char:
    if char not in list_word and char != ' ':
        if count < list_char.count(char):
            count = list_char.count(char)
            text = char
        elif count == list_char.count(char):
            if char < text:
                count = list_char.count(char)
                text = char
        list_word += char
print(text)
