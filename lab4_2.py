# Користувачем вводяться наступні дані: у першому рядку міститься кількість рядків n, а потім - вводяться n рядків слів. 
# Надрукуйте слово, яке в тексті зустрічається найчастіше. Якщо таких слів є декілька,
# надрукуйте слово, яке в алфавітному порядку розташоване раніше.

n = int(input())

word_count = {}

for _ in range(n):
    words = input().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

max_count = 0
min_word = ''

for word, count in word_count.items():
    if count > max_count or (count == max_count and word < min_word):
        max_count = count
        min_word = word

print(min_word)
