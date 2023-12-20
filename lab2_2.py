
a = int(input())
b = int(input())
c = int(input())
a, b, c = sorted([a, b, c])
if a + b <= c:
    print('impossible') 
elif c**2 == (a**2) + (b**2):
    print('rectangular')
elif ((a**2) + (b**2) - (c**2)) / (2 * a * b) > 0:
    print('acute')
else:
    print('obtuse')