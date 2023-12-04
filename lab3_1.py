def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

n = int(input("Введіть ціле число n: "))
result = 0

for i in range(1, n + 1):
    result += factorial(i)

print("Сума факторіалів від 1 до", n, "дорівнює", result)
