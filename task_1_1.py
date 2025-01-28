def vigenere_encrypt(text, key):
    cipher_text = []
    # Заведемо лічильник для "ходження" по ключу
    key_index = 0
    key_length = len(key)

    for ch in text:
        if ch.isalpha():
            # Визначаємо зсув для поточної літери ключа.
            # Переводимо символ ключа до нижнього регістру, 
            # щоб позиція була від 'a' (код 97) до 'z' (код 122).
            shift = ord(key[key_index % key_length].lower()) - ord('a')

            # Якщо символ – велика літера
            if ch.isupper():
                # нормуємо від A (код 65) до Z (код 90)
                base = ord('A')
                new_char = chr((ord(ch) - base + shift) % 26 + base)
                cipher_text.append(new_char)
            else:
                # інакше (мала літера)
                base = ord('a')
                new_char = chr((ord(ch) - base + shift) % 26 + base)
                cipher_text.append(new_char)

            # Переходимо до наступної літери ключа
            key_index += 1
        else:
            # Якщо символ не літера (пробіл, цифра, розділовий знак тощо),
            # додаємо його без змін і НЕ зрушуємо key_index.
            cipher_text.append(ch)

    return "".join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    original_text = []
    key_index = 0
    key_length = len(key)

    for ch in cipher_text:
        if ch.isalpha():
            # Визначаємо зсув (аналогічно до шифрування)
            shift = ord(key[key_index % key_length].lower()) - ord('a')

            if ch.isupper():
                base = ord('A')
                # Для дешифрування віднімаємо зсув
                new_char = chr((ord(ch) - base - shift) % 26 + base)
                original_text.append(new_char)
            else:
                base = ord('a')
                new_char = chr((ord(ch) - base - shift) % 26 + base)
                original_text.append(new_char)

            key_index += 1
        else:
            original_text.append(ch)

    return "".join(original_text)

def main():
    # Зчитаємо текст з файлу plain.txt
    with open("plain.txt", "r", encoding="utf-8") as f:
        text = f.read()

    key = "CRYPTOGRAPHY"  # Ключ можна лишити в будь-якому регістрі.

    # Шифруємо
    encrypted_text = vigenere_encrypt(text, key)
    print("Зашифрований текст:", encrypted_text)

    # Розшифровуємо, щоб перевірити
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Розшифрований текст:", decrypted_text)

if __name__ == "__main__":
    main()
