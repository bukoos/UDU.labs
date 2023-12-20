# Дано послідовність натуральних чисел, що завершується числом 0. 
# Визначте найбільше число елементів цієї послідовності, що йдуть підряд один за одним, і дорівнюють один одному. 
# Вводиться послідовність цілих чисел, що закінчується числом 0 
# (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).
n = 1
nx = 0
pos = -1
prev = -1
while pos != 0:
    pos = int(input())
    if prev != -1:
        if pos == prev:
            n += 1
        else:
            if nx < n:
                nx = n
            n = 1
    prev = pos
print(nx)
