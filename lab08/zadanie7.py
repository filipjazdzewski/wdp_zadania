def dec_to_bin(num):
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    return dec_to_bin(num // 2) + str(num % 2)


result = int(input('Podaj liczbe naturalna:'))
print(dec_to_bin(result))

#  dec_to_bin(11 // 2) + str(11 % 2) = '1' + dec_to_bin(5 // 2) + str(5 % 2) =
# = '1' + '1' + dec_to_bin(2 // 2) + str(2 % 2) =
# = '0' + '1' + '1' + dec_to_bin(1 // 2) + str(1 % 2) =
# = '1' + '0' + '1' + '1' = '1011'
