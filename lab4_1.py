# У трьох автобусах розсадили дітей так, що їх кількість в різних автобусах різна. 
# Яку найменшу кількість дітей потрібно пересадити, щоб у кожному автобусі їх було порівно? 
# У першому рядку задано три натуральних числа, не більших за 100 - кількість дітей у першому, другому та третьому автобусах.
# Виведіть одне число - найменшу кількість дітей, яких потрібно пересадити. Якщо це зробити не можливо, то виведіть NO SOLUTIONS.

bus_children = tuple(map(int, input().split()))

total_children = sum(bus_children)
avg_children = total_children // 3

if total_children % 3 != 0:
    print("NO SOLUTIONS")
else:
    transfers = 0
    for i in range(3):
        diff = avg_children - bus_children[i]
        if diff > 0:
            transfers += diff

    print(transfers)

