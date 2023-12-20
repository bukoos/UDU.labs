#Вводиться додатне ціле трицифрове число. Знайти суму цифр числа. Буртенко 31І
number = int(input("Введіть трицифрове число: "))

digit_1 = number // 100  
digit_2 = (number // 10) % 10
digit_3 = number % 10  

sum_of_digits = digit_1 + digit_2 + digit_3

print("Сума цифр у числі", number, "дорівнює", sum_of_digits)
