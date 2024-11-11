#A

a = input()
while a != 'Три!':
	print('Режим ожидания...')
	a = input()
print('Ёлочка, гори!')

#B

count = 0
while (s := input()) != 'Приехали!':
    if 'зайка' in s:
        count += 1
print(count)

#C

a = int(input())
b = int(input())
for i in range(a, b + 1):
	print(i, end=' ')

#D

a = int(input())
b = int(input())
if a < b:
	for i in range(a, b + 1):
		print(i, end=' ')
else:
	for i in range(a, b - 1, -1):
		print(i, end=' ')

#E

summa = 0
while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    summa += price
print(summa)

#F

a = int(input())
b = int(input())
for i in range(min(a, b), 0, -1):
	if b % i == 0 and a % i == 0:
		print(i)
		break

#G

a, b = a1, b1 = int(input()), int(input())
while a != 0:
    a, b = b % a, a
print(a1 * b1 // (a + b))

#H

a = input()
b = int(input())
for i in range(1, b + 1):
	print(a)


#I

a = int(input())
b = 1
for i in range(1, a + 1):
	b *= i
print(b)

#J

x, y = 0, 0
while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n     
print(y)
print(x)

#K

a = int(input())
b = 0
while a != 0:
	b += a % 10
	a = a // 10
print(b)

#L

a = int(input())
b = 0
c = 0
while a != 0:
	c = a % 10
	b = max(b, c)
	a = a // 10
print(b)

#M

count = int(input())
first = 'яяяяяяяя'
for _ in range(count):
    name = input()
    if name < first:
        first = name
print(first)

#N

num = int(input())
divisor = 2
prime = True
if -1 <= num <= 1:
    prime = False
else:
    while divisor ** 2 <= num and prime is True:
        if num % divisor == 0:
            prime = False
        else:
            divisor = divisor + 1
if prime is True:
    print('YES')
else:
    print('NO')

#O

b = int(input())
count_ = 0
for i in range(b):
	a = input()
	if 'зайка' in a:
		count_ += 1
print(count_)

#P

n = str(input())
if len(n) % 2 == 0:
	a = n[:len(n) // 2]
	b = n[:(len(n) // 2 - 1):-1]
else:
	a = n[:len(n) // 2 + 1]
	b = n[:(len(n) // 2 - 1):-1]
if a == b:
	print('YES')
else:
	print('NO')