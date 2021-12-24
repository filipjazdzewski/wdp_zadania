
k = 10
m = 50

while k != 0:
    if k < 5:
        k -= 1
        m += k
    else:
        k -= 2
        m -= k

print(m)


k = 10
m = 50

while True:
    if k < 5:
        k -= 1
        m += k
    else:
        k -= 2
        m -= k
    if not k != 0:
        break

print(m)