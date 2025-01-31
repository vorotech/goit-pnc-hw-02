#!/usr/bin/env python
# coding: utf-8

import math

def transposition_encrypt(text, key):
    """
    Шифрування перестановочним методом, зберігаючи пробіли.
    """
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)  # Округлення вгору

    # Заповнюємо таблицю разом із пробілами
    padded_text = text.ljust(num_cols * num_rows, "_")  # Використовуємо "_" як заповнювач
    table = [padded_text[i:i + num_cols] for i in range(0, len(padded_text), num_cols)]

    # Отримуємо порядок колонок (сортуємо ключ)
    sorted_key = sorted((ch, i) for i, ch in enumerate(key))
    key_order = [i for _, i in sorted_key]  # Індекси у відсортованому порядку

    # Читаємо таблицю по стовпцях у порядку key_order
    encrypted_text = ''.join(''.join(row[col] for row in table) for col in key_order)

    return encrypted_text


def transposition_decrypt(encrypted_text, key):
    """
    Дешифрування перестановочним методом, відновлюючи пробіли.
    """
    num_cols = len(key)
    num_rows = math.ceil(len(encrypted_text) / num_cols)

    # Відновлюємо порядок колонок
    sorted_key = sorted((ch, i) for i, ch in enumerate(key))
    key_order = [i for _, i in sorted_key]  # Індекси у відсортованому порядку

    # Визначаємо розмірність кожного стовпця (скільки символів у ньому)
    col_sizes = [num_rows] * num_cols
    extra_chars = len(encrypted_text) % num_cols  # Якщо є "неповні" стовпці
    for i in range(extra_chars):
        col_sizes[key_order[i]] += 1  # Додаємо зайві символи у перші стовпці

    # Відновлюємо початкову таблицю (заповнюємо стовпці)
    columns = [''] * num_cols
    index = 0
    for col_index in key_order:  # Заповнюємо за зашифрованим порядком
        col_len = col_sizes[col_index]
        columns[col_index] = encrypted_text[index:index + col_len]
        index += col_len

    # Відновлення вихідного тексту з таблиці
    table = [''] * num_rows
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(columns[col]):
                table[row] += columns[col][row]

    return ''.join(table).replace("_", " ")


def double_transposition_encrypt(text, key1, key2):
    """
    Подвійна перестановка (шифрування), зберігаючи пробіли.
    """
    first_pass = transposition_encrypt(text, key1)
    second_pass = transposition_encrypt(first_pass, key2)
    return second_pass


def double_transposition_decrypt(encrypted_text, key1, key2):
    """
    Подвійна перестановка (дешифрування), відновлюючи пробіли.
    """
    first_pass = transposition_decrypt(encrypted_text, key2)
    second_pass = transposition_decrypt(first_pass, key1)
    return second_pass


def main():
    # Читаємо текст із файлу plain.txt, зберігаючи пробіли
    with open("plain.txt", "r", encoding="utf-8") as f:
        text = f.read()  # Пробіли залишаються!

    key1 = "SECRET"
    key2 = "CRYPTO"

    # Шифруємо
    encrypted_text = double_transposition_encrypt(text, key1, key2)
    print("Зашифрований текст:", encrypted_text)

    # Розшифровуємо
    decrypted_text = double_transposition_decrypt(encrypted_text, key1, key2)
    print("Розшифрований текст:", decrypted_text)


if __name__ == "__main__":
    main()
