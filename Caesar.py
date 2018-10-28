from string import ascii_lowercase

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'*3

def encrypt():
    key = int(input('Введите ключ для шифрования: '))

    print('Введите сообщение: ')
    input_string = input().lower()

    output_string = []

    for letter in input_string:
        if letter.isspace():
            output_string.append(' ')
        elif letter.isalpha():
            output_string.append(alphabet[alphabet.index(letter)+key])
        elif letter.isdigit():
            continue
        else:
            output_string.append(letter)

    print('Зашифрованное сообение: {}'. format(''.join(output_string)))
    return ''.join(output_string)


def decipher():
    key = int(input('Введите ключ для дешифровки: '))

    print('Введите сообщение: ')
    input_string = input().lower()

    output_string = []

    for letter in input_string:
        if letter.isspace():
            output_string.append(' ')
        elif letter.isalpha():
            output_string.append(alphabet[alphabet.index(letter) - key])
        elif letter.isdigit():
            continue
        else:
            output_string.append(letter)

    print('Encrypted message: {}'.format(''.join(output_string)))

encrypt()
decipher()

