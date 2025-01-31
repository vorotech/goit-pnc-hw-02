#!/usr/bin/env python
# coding: utf-8

# Імпортуємо методи шифрування з файлів
from task_1_1 import vigenere_encrypt, vigenere_decrypt
from task_3_1 import table_encrypt, table_decrypt

def main():
    # Читаємо текст із файлу plain.txt
    with open("plain.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Використовувані ключі
    vigenere_key = "CRYPTOGRAPHY"
    table_key = "CRYPTO"

    # Спочатку використаємо шифр Віженера
    encrypted_text_vigenere = vigenere_encrypt(text, vigenere_key)
    
    # Потім зашифруємо табличним шифром    
    encrypted_text_final = table_encrypt(encrypted_text_vigenere, table_key)

    print("Зашифрований текст:", encrypted_text_final)

    
    # Розшифровуємо в зворотньому порядку
    decrypted_text_table = table_decrypt(encrypted_text_final, table_key)

    # Потім розшифровуємо шифром Віженера
    decrypted_text_final = vigenere_decrypt(decrypted_text_table, vigenere_key)    

    print("Розшифрований текст:", decrypted_text_final)

if __name__ == "__main__":
    main()
