#!/usr/bin/env python
# coding: utf-8

def create_matrix(key):
    matrix = []
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def table_encrypt(text, key):
    matrix = create_matrix(key)
    encrypted_text = []

    for char in text.upper():
        if char.isalpha() and char != 'Z':
            for row in matrix:
                if char in row:
                    col_index = row.index(char)
                    row_index = matrix.index(row)
                    encrypted_text.append(matrix[(row_index + 1) % 5][col_index])
                    break
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def table_decrypt(encrypted_text, key):
    matrix = create_matrix(key)
    decrypted_text = []

    for char in encrypted_text:
        if char.isalpha() and char != 'Z':
            for i, row in enumerate(matrix):
                if char in row:
                    row_index = i
                    col_index = row.index(char)
                    decrypted_text.append(matrix[(row_index - 1) % 5][col_index])
                    break
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


def main():
    # Читаємо текст із файлу plain.txt, зберігаючи пробіли
    with open("plain.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    key = "MATRIX"

    # Шифруємо
    encrypted_text = table_encrypt(text, key)
    print("Зашифрований текст:", encrypted_text)

    # Розшифровуємо
    decrypted_text = table_decrypt(encrypted_text, key)
    print("Розшифрований текст:", decrypted_text)



if __name__ == "__main__":
    main()
