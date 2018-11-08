from string import ascii_lowercase
import tkinter as tk

root = tk.Tk()
frame_encrypt = tk.Frame()
frame_decipher = tk.Frame()
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'*3

def encrypt():

    key = int(key1.get())
    input_string = input_text1.get(1.0, 'end').lower()
    output_string = list()

    for letter in input_string:
        if letter.isspace():
            output_string.append(' ')
        elif letter.isalpha():
            output_string.append(alphabet[alphabet.index(letter)+key])
        else:
            output_string.append(letter)

    output_text1.delete(1.0, 'end')
    output_text1.insert(1.0, ''.join(output_string))


def decipher():

    key = int(key2.get())
    input_string = input_text2.get(1.0, 'end').lower()
    output_string = list()

    for letter in input_string:
        if letter.isspace():
            output_string.append(' ')
        elif letter.isalpha():
            output_string.append(alphabet[alphabet.index(letter) - key])
        else:
            output_string.append(letter)

    output_text2.delete(1.0, 'end')
    output_text2.insert(1.0, ''.join(output_string))

subtitle1 = tk.Label(frame_encrypt, text = 'Введите ключ и сообщение для шифрования')
key1 = tk.Entry(frame_encrypt)
input_text1 = tk.Text(frame_encrypt, width = '30')
output_text1 = tk.Text(frame_encrypt, width = '30')
btn_encrypt1 = tk.Button(frame_encrypt, text = 'Зашифровать', command = encrypt)

subtitle2 = tk.Label(frame_decipher, text = 'Введите ключ и зашифрованнный текст')
key2 = tk.Entry(frame_decipher)
input_text2 = tk.Text(frame_decipher, width = '30')
output_text2 = tk.Text(frame_decipher, width = '30')
btn_encrypt2 = tk.Button(frame_decipher, text = 'Расшифровать', command = decipher)

frame_encrypt.pack(pady = 10)
subtitle1.pack()
key1.pack(pady = 7)
input_text1.pack(side = 'left')
output_text1.pack(side = 'right')
btn_encrypt1.pack(pady = 100, padx = 7)

frame_decipher.pack(pady = 10)
subtitle2.pack()
key2.pack(pady = 7)
input_text2.pack(side = 'left')
output_text2.pack(side = 'right')
btn_encrypt2.pack(pady = 100, padx = 7)

root.mainloop()
