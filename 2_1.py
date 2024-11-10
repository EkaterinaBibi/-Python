#A

print("Привет, Яндекс!")

#B

name = input("Как Вас зовут?")
print("Привет,", name)

#C

line = input()
print(line)
print(line)
print(line)

#D

money = int(input())
price = int(2.5 * 38)
print(money - price)

#E

price = int(input())
weight = int(input())
money = int(input())
print(money - (price * weight))

#F

good = input()
price = int(input())
weight = int(input())
cash = int(input())
print('Чек')
print(f'{good} - {weight}кг - {price}руб/кг')
print(f'Итого: {price * weight}руб')
print(f'Внесено: {cash}руб')
print(f'Сдача: {cash - price * weight}руб')

#G

n = int(input())
name = str("Купи слона!") + '\n'
print(name * n)

#H

n = int(input())
name = 'Я больше никогда не буду писать "' + input() + '"!'
name = name + '\n'
print(name * n)

#I

n = int(input())
m = int(input())
v = n / 2 * m
print(int(v))

#J

name = input()
number = int(input())
n_list = number % 10
n_locker = number // 10 % 10
n_bed = number // 100
print(f'Группа №{n_bed}.')
print(f'{n_list}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {n_locker}.')

#K

n = int(input())
a = str(n // 1000)
b = str(n // 100 % 10)
c = str(n // 10 % 10)
d = str(n % 10)
print(int(b + a + d + c))

#L

num1 = int(input())
num2 = int(input())
res1 = ((num1 % 10) + (num2 % 10)) % 10
res2 = ((num1 // 10) + (num2 // 10)) % 10
res3 = ((num1 // 100) + (num2 // 100)) % 10
print(str(res3) + str(res2) + str(res1))

#M

children = int(input())
candy = int(input())
print(candy // children)
print(candy - candy // children * children)

#N

red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#O

n = int(input())
m = int(input())
t = int(input())
hours = (n + (m + t) // 60) % 24
m = (m + t) % 60
print(f'{hours:02d}:{m:02d}')

#P

a = int(input())
b = int(input())
c = int(input())
print(f'{((b - a) / c):.2f}')
