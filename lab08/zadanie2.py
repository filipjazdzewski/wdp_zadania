def string_reversal(string):
    if len(string) > 1:
        return string[0] + string_reversal(string[1:])
    return string


result = input('Podaj ciag znakow:')
print(string_reversal(result))

# string_reversal(kolos) = 'k' + string_reversal(olos) = 'o' + 'k' + string_reversal(los) =
# = 'l' + 'o' + 'k' + string_reversal(os) = 'o' + 'l' + 'o' + 'k' + string_reversal(s) =
# = 's' + 'o' + 'l' + 'o' + 'k' = 'solok'
