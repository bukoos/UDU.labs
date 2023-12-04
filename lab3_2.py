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
