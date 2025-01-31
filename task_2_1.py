#!/usr/bin/env python
# coding: utf-8

def transposition_encrypt(text, key):
    num_cols = len(key)
    num_rows = len(text) // num_cols + (1 if len(text) % num_cols else 0)
    padded_text = text.ljust(num_cols * num_rows)
    encrypted_text = [''] * num_cols

    for col in range(num_cols):
        for row in range(num_rows):
            encrypted_text[col] += padded_text[row * num_cols + col]

    return ''.join(encrypted_text)


def transposition_decrypt(encrypted_text, key):
    num_cols = len(key)
    num_rows = len(encrypted_text) // num_cols

    # Створюємо список із порожніми рядками
    table = [""] * num_rows

    # Заповнюємо таблицю по стовпцях
    index = 0
    for col in range(num_cols):
        for row in range(num_rows):
            table[row] += encrypted_text[index]
            index += 1

    # Тепер читаємо таблицю по рядках
    return "".join(table).strip()

def main():
    # Зчитаємо текст з файлу plain.txt
    with open("plain.txt", "r", encoding="utf-8") as f:
        text = f.read()

    key = "SECRET"

    # Шифруємо
    encrypted_text = transposition_encrypt(text, key)
    print("Зашифрований текст:", encrypted_text)

    # Розшифровуємо, щоб перевірити
    decrypted_text = transposition_decrypt(encrypted_text, key)
    print("Розшифрований текст:", decrypted_text)

if __name__ == "__main__":
    main()
