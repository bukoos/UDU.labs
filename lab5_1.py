def perfect_num(number):
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number

def check_perfect_number():
    user_input = int(input("Введіть число: "))
    result = perfect_num(user_input)
    return result

result = check_perfect_number()
if result:
    print("True")
else:
    print("False")