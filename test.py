print('Hello')
a = input('введите ряд чисел через пробел: ').split()
first_a = a[0]
last_a = a[len(a)-1]
a[len(a)-1] = a[0]
a[0] = last_a
a.append(int(first_a) + int(last_a))
print(a)
b=15
print(b)
"""
комментарий многострочный
вот еще одна строка
"""