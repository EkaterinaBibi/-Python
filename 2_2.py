#A

name = input()
quatoin = input()
print('Как Вас зовут?')
print(f'Здравствуйте, {name}!')
print('Как дела?')
if quatoin == 'хорошо':
	print('Я за вас рада!')
else:
	print('Всё наладится!')

#B

p = int(input())
v = int(input())
if p > v:
	print('Петя')
else:
	print('Вася')

#C

p = int(input())
v = int(input())
t = int(input())
if p == max(p, v, t):
	print('Петя')
elif t == max(p, v, t):
	print('Толя')
else:
	print('Вася')

#D

p = int(input())
v = int(input())
t = int(input())
name_1 = max(p, v, t)
name_3 = min(p, v, t)
name_2 = p + v + t - max(p, v, t) - min(p, v, t)
if name_1 == p:
	print('1. Петя')
elif name_1 == t:
	print('1. Толя')
else:
	print('1. Вася')
if name_2 == p:
	print('2. Петя')
elif name_2 == t:
	print('2. Толя')
else:
	print('2. Вася')
if name_3 == p:
	print('3. Петя')
elif name_3 == t:
	print('3. Толя')
else:
	print('3. Вася')

#E

n = int(input())
m = int(input())
p = 7 - 3 + 2 + n
v = 6 + 3 + 5 - 2 + m
if p > v:
	print('Петя')
else:
	print('Вася')

#F

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print('YES')
else:
	print('NO')

#G

n = int(input())
if n // 1000 == n % 10 and n // 100 % 10 == n // 10 % 10:
	print('YES')
else:
	print('NO')

#H

text = str(input())
if 'зайка' in text:
	print('YES')
else:
	print('NO')

#I

a = input()
b = input()
c = input()
print(min(a, b, c))

#J

n = int(input())
n1 = n // 100 % 10 + n // 10 % 10
n2 = n // 10 % 10 + n % 10
print(str(max(n1, n2)) + str(min(n1, n2)))

#K

n = int(input())
n1 = n // 100 % 10
n2 = n // 10 % 10
n3 = n % 10
if (max(n1, n2, n3) + min(n1, n2, n3)) == (n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3)) * 2:
	print('YES')
else:
	print('NO')

#L

a = int(input())
b = int(input())
c = int(input())
if (a + b) > c and (c + b) > a and (a + c) > b:
	print('YES')
else:
	print('NO')

#M

a = int(input())
b = int(input())
c = int(input())
if a % 10 == b % 10 == c % 10:
	print(a % 10)
else:
	print(a // 10)

#N

num = int(input())
first = num // 100
second = num // 10 % 10
third = num % 10
middle = first + second + third - min(first, second, third) - max(first, second, third)
if min(first, second, third) != 0:
    minimal = min(first, second, third) * 10 + middle
elif middle != 0:
    minimal = middle * 10
else:
    minimal = max(first, second, third) * 10
maximal = max(first, second, third) * 10 + middle
print(minimal, maximal)

#O

a = int(input())
b = int(input())
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10
c = (a1 + a2 + b1 + b2 - max(a1, a2, b1, b2) - min(a1, a2, b1, b2)) % 10
print(max(a1, a2, b1, b2) * 100 + c * 10 + min(a1, a2, b1, b2))

#P

petya = int(input())
vasya = int(input())
tolya = int(input())
first = max(petya, vasya, tolya)
third = min(petya, vasya, tolya)
second = petya + vasya + tolya - first - third
if first == petya:
    first_name = 'Петя'
elif first == vasya:
    first_name = 'Вася'
else:
    first_name = 'Толя'
if second == petya:
    second_name = 'Петя'
elif second == vasya:
    second_name = 'Вася'
else:
    second_name = 'Толя'
if third == petya:
    third_name = 'Петя'
elif third == vasya:
    third_name = 'Вася'
else:
    third_name = 'Толя'
print(f'{first_name: ^24}')
print(f'{second_name: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_name: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')