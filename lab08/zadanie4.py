def newton_symbol(n, k):
    if k < 0 or k > n:
        return None
    if k == 0 or k == n:
        return 1
    return newton_symbol(n-1, k-1) + newton_symbol(n-1, k)


num_n = int(input('Podaj n:'))
num_k = int(input('Podaj k:'))
print(newton_symbol(num_n, num_k))
