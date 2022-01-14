cipher_file = open('szyfr.txt', 'r')
decipher_file = open('odszyfr.txt', 'w')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

my_arr = cipher_file.read().lower().split()


def decipher(arr, alphabet):
    deciphered_word = ''
    for i in range(0, len(arr), 2):
        shift = int(arr[i + 1])
        for letter in arr[i]:
            for j in range(len(alphabet)):
                if letter == alphabet[j]:
                    deciphered_word += alphabet[(j + shift) % len(alphabet)]
        deciphered_word += ' '
    return deciphered_word


decipher_file.write(decipher(my_arr, alphabet))
