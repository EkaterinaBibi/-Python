#A

text = input()
list_ = []
for i in text:
    if i not in list_:
        print(i, end='')
        list_ += i

#B

word_1 = input()
word_2 = input()
text = []
for char in word_1:
    if char in word_2 and char not in text:
        text += char
        print(char, end='')

#C

n = int(input())
list_ = []
for i in range(n):
    text = input().split()
    for word in range(len(text)):
        if text[word] not in list_:
            list_ += [text[word]]
            print(text[word])

#D

n = int(input())
m = int(input())
lastname_ = []
count = 0
list_ = []
for i in range(n):
    lastname = input()
    lastname_ += [lastname]
for j in range(m):
    lastname = input()
    lastname_ += [lastname]
for char in lastname_:
    if lastname_.count(char) == 2 and char not in list_:
        count += 1
        list_ += [char]
if count == 0:
    print('Таких нет')
else:
    print(count)

#E

n = int(input())
m = int(input())
lastname_ = []
count = 0
for i in range(n):
    lastname = input()
    lastname_ += [lastname]
for j in range(m):
    lastname = input()
    lastname_ += [lastname]
for char in lastname_:
    if lastname_.count(char) == 1:
        count += 1
if count == 0:
    print('Таких нет')
else:
    print(count)

#F

n = int(input())
m = int(input())
lastname_ = []
count = 0
listin = []
for i in range(n):
    lastname = input()
    lastname_ += [lastname]
for j in range(m):
    lastname = input()
    lastname_ += [lastname]
for char in lastname_:
    if lastname_.count(char) == 1:
        count += 1
        listin += [char]
if count == 0:
    print('Таких нет')
else:
    list_ = listin.sort()
    for k in listin:
        print(k)

#G

MORZE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K':
         '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

for char in input():
    if char != ' ':
        print(MORZE[char.upper()], end=' ')
    else:
        print()

#H

porridge_eaters = {}
for _ in range(int(input())):
    string = input()
    eater, *porridges = string.split()
    porridge_eaters[eater] = porridges
porridge = input()
names = []
for name in porridge_eaters:
    if porridge in porridge_eaters[name]:
        names.append(name)
if not names:
    print('Таких нет')
else:
    names.sort()
    for name in names:
        print(name)

#I

list_ = []
text_for_count = []
while (text := input()) != '':
    text = text.split()
    text_for_count += text
    for word in range(len(text)):
        if text[word] not in list_:
            list_ += [text[word]]
for i in list_:
    print(i, text_for_count.count(i))

#J

text = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'Ь': '', 'Ъ': ''}
n = input()
text_new = ''
for char in n:
    char_copy = char.upper()
    if char_copy in text:
        if char.isupper():
            char = text[char_copy]
        else:
            char = text[char_copy].lower()
    text_new += char
print(text_new)