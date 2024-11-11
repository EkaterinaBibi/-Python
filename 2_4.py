#A

n = int(input())
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(i * j, end=' ')
	print()

#B

n = int(input())
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(f'{j} * {i} = {i * j}')

#C

n = int(input())
a = 1
c = 1
while c <= n:
	for i in range(a):
		if c > n:
			break
		print(c, end=' ')
		c += 1
	print()
	a += 1

#D

n = int(input())
c = 0
for i in range(n):
	a = int(input())
	while a != 0:
		c += a % 10
		a //= 10
print(c)

#E

n = int(input())
count = 0
for i in range(n):
	c = 0
	while (a := input()) != 'ВСЁ':
		if a == 'зайка' and c == 0:
			count += 1
			c = 1
print(count)

#F

n = int(input())
first = int(input())
for i in range(n - 1):
	second = int(input())
	while first != 0:
		if first < second:
			first, second = second, first
		first = first % second
	first = second
print(first)

#G

n = int(input())
for i in range(1, n + 1):
	for j in range(i + 2, 0, -1):
		print(f'До старта {j} секунд(ы)')
	print(f'Старт {i}!!!')

#H

n = int(input())
win = ''
sum_max = 0
for i in range(n):
	name = input()
	m = int(input())
	sum_ = 0
	while m != 0:
		sum_ += m % 10
		m //= 10
	if sum_ >= sum_max:
		sum_max = sum_
		win = name
print(win)

#I

n = int(input())
max_ = 0
sum_ = ''
for i in range(n):
	a = int(input())
	while a > 0:
		max_ = max(max_, a % 10)
		a //= 10
	sum_ += str(max_)
	max_ = 0
print(sum_)

#J

print('А Б В')
n = int(input())
for i in range(1, n - 1):
	for j in range(1, n - 1):
		if n - i - j > 0:
			print(i, j, n - i - j)

#K

n = int(input())
count = 0
for i in range(n):
	name = int(input())
	if name == 1:
		continue
	for j in range(2, int(name ** 0.5) + 1):
		if name % j == 0:
			break
	else:
		count += 1
print(count)

#L

n = int(input())
m = int(input())
len_ = len(str(n * m))
c = 0
for i in range(n):
	for j in range(m):
		c += 1
		print(f'{c:>{len_}}', end=' ')
	print()

#M

height = int(input())
width = int(input())
cell_width = len(str(width * height))
number = 1
for row in range(height):
    number = row + 1
    for _ in range(width):
        print(f'{number:>{cell_width}}', end=' ')
        number += height
    print()

#N

n = int(input())
m = int(input())
len_ = len(str(n * m))
count = 0
len_number = 1
for i in range(n):
	for j in range(m):
		if len_number % 2 != 0:
			count += 1
		else:
			count -= 1
		print(f'{count:>{len_}}', end=' ')
	len_number += 1
	if len_number % 2 != 0:
		count = m * (len_number - 1)
	else:
		count = m * len_number + 1
	print()

#O

n = int(input())
m = int(input())
len_ = len(str(n * m))
for i in range(n):
	for j in range(m):
		if j % 2 == 0:
			count = j * n + i + 1
		else:
			count = n * (j + 1) - i
		print(f'{count:>{len_}}', end=' ')
	print()

#P

n = int(input())
m = int(input())
len_ = m * n + n - 1
for i in range(n):
	for j in range(n):
		count = (i + 1) * (j + 1)
		print(f'{count:^{m}}', end='')
		if j != n - 1:
			print('|', end='')
		else:
			print()
	if i + 1 != n:
		print('-' * len_)
