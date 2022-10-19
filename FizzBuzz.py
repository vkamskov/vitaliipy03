fizz, buzz, x = list(map(int, input('Введите 3 числа через пробел: ') .split()))

for i in range(1, x + 1):
    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
    elif i % fizz == 0:
        print('F', end=' ')
    elif i % buzz == 0:
        print('B', end=' ')
    else:
        print(i, end=' ')
