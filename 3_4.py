#A

text = input()
text = text.split()
for i in range(len(text)):
    print(f'{i + 1}. {text[i]}')

#B

grupp1 = input()
grupp1 = grupp1.split(', ')
grupp2 = input()
grupp2 = grupp2.split(', ')
for i in zip(grupp1, grupp2):
    print(f'{i[0]} - {i[1]}')

#C

from itertools import count
a, b, c = [float(i) for i in input().split()]
for j in count(a, c):
    if j > b:
        break
    print(f'{j:.2f}')

#D

text = input()
text = text.split()
for i in range(len(text)):
    for j in range(i + 1):
        print(text[j], end=' ')
    print()

#E

text1, text2, text3 = input(), input(), input()
text = text1.split(', ') + text2.split(', ') + text3.split(', ')
text.sort()
for i in range(len(text)):
    print(f'{i + 1}. {text[i]}')

#F

from itertools import product
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
mastys = ['пик', 'треф', 'бубен', 'червей']
name = input()
mastys.remove(name)
for card, masty in product(cards, mastys):
    print(card, masty)

#G

from itertools import combinations
n = int(input())
name = []
for i in range(n):
    name += input().split()
for name1, name2 in list(combinations(name, 2)):
    print(f'{name1} - {name2}')

#H

from itertools import cycle
n = int(input())
name = []
count = 0
for i in range(n):
    name += input().split()
m = int(input())
for text in cycle(name):
    if count < m:
        print(text)
        count += 1
    else:
        break

#I

from itertools import product, islice
number = int(input())
numbers = [n * m for n, m in product(range(1, number + 1), repeat=2)]
for k in range(number):
    print(*islice(numbers, k * number, (k + 1) * number))

#J

from itertools import product
n = int(input())
print('А Б В')
for i, j in product(range(1, n - 1), range(1, n - 1)):
    if i + j >= n:
        continue
    else:
        print(f'{i} {j} {n - i - j}')