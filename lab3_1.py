# Дано ціле число n, яке вводить користувач. Необхідно обчислити значення виразу 1! +2! +3! + … + n!.
n = int(input("Введіть ціле число n: "))
result = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    result += factorial

print("Сума факторіалів від 1 до", n, "дорівнює", result)
