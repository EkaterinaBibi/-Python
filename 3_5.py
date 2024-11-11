#A

from itertools import accumulate
from sys import stdin
sum_ = 0
list_ = []
for text in stdin:
    list_ += [int(n) for n in text.split()]
for i in accumulate(list_):
    sum_ = i
print(sum_)

#B

from sys import stdin
text = stdin.read().split('\n')
hight = 0
count = 0
for line in text:
    if line:
        name, then, now = line.split()
        hight += int(now) - int(then)
        count += 1
print(round(hight / count))

#C

from sys import stdin
for text in stdin:
    if text[0] != '#':
        print(text.split('#')[0].rstrip('\n'))

#D

from sys import stdin
text = stdin.readlines()
subject = text[-1].strip('\n').lower()
objects = text[:-1]
for line in objects:
    if line.lower().find(subject) + 1:
        print(line.strip('\n'))

#E

from sys import stdin
text = stdin.readlines()
listin = []
for line in text:
    for word in line.replace('\n', '').split():
        if word.lower() == word.lower()[::-1]:
            listin.append(word)
print('\n'.join(sorted(set(listin))))

#F

alphabet = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''}
with open('transliteration.txt', 'w', encoding='UTF-8') as file_out:
    with open('cyrillic.txt', encoding='UTF-8') as file_in:
        for text in file_in:
            for char in text:
                word = char.upper()
                if word in alphabet:
                    if char.isupper():
                        char = alphabet[word].capitalize()
                    else:
                        char = alphabet[word].lower()
                else:
                    char = char
                print(char, end='', file=file_out)

#G

with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]
print(len(numbers))
print(len([n for n in numbers if n > 0]))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(f'{(sum(numbers) / len(numbers)):.2f}')

#H

file_1 = input()
file_2 = input()
file_3 = input()
with open(file_1, encoding='UTF-8') as file_in:
    text_1 = set([line for line in file_in.read().split()])
with open(file_2, encoding='UTF-8') as file_in:
    text_2 = set([line for line in file_in.read().split()])
text = text_1 ^ text_2
with open(file_3, 'w', encoding='UTF-8') as file_out:
    print('\n'.join(sorted(text)), file=file_out)

#I

file_1, file_2 = input(), input()
with open(file_1, encoding="UTF-8") as file_1:
    text = file_1.read()

while text.find("\t") + 1:
    text = text.replace("\t", "")
while text.find("  ") + 1:
    text = text.replace("  ", " ")

text = "\n".join(line.strip() for line in text.split("\n") if line)

with open(file_2, "w", encoding="UTF-8") as file_2:
    file_2.write(text)

#J

file_ = input().strip()
n = int(input())
text = []
with open(file_, encoding='UTF-8') as file_in:
    for line in file_in:
        text.append(line)
for line in text[-n:]:
    print(line.strip())