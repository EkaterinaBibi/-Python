#A

def make_list(length, value=0):
    return [value for _ in range(length)]

#B

def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for i in range(size)] for j in range(size)]
    else:
        return [[value for i in range(size[0])] for j in range(size[1])]

#C

def gcd(*args):
    a = list(args)
    while len(a) > 1:
        while a[1]:
            a[0], a[1] = a[1], a[0] % a[1]
        a.pop(1)
    return a[0]

#D

def month(number, language='ru'):
    MONTH = {
        'en': [
            'January', 'February', 'March',
            'April', 'May', 'June',
            'July', 'August', 'September',
            'October', 'November', 'December'
        ],
        'ru': [
            'Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь'
        ]
    }
    return MONTH[language][number - 1]

#E

def to_string(*data, sep=' ', end='\n'):
    return sep.join(str(i) for i in data) + end
