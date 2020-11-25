# Лабораторная работа номер 9
# Написать программу, реализующую меню
# 1. Ввод строки
# 2. Настройка ключа для шифра
# 3. Шифрование строки
# 4. Расшифрованиея строки
# 5. Напечатать таблицу
# 6. Выход
# написал Щербина МА иу7-15

def gen_alphabet():
    return "".join([chr(i) for i in range(32, 127)])

def shift_string(string, n):
    return (string + string[:n])[n:]

def main():
    alphabet = gen_alphabet()
    zero_offset = ord(alphabet[0])
    to_encrypt = "teststring"
    encrypted = ""
    key = "abracadabra"
    while True:
        print(
            """
    # 1. Ввод строки
    # 2. Настройка ключа для шифра
    # 3. Шифрование строки
    # 4. Расшифрование строки
    # 5. Напечатать таблицу
    # 6. Выход
        """
        )
        option = int(input(">>> option: "))
        if option == 1:  # input string to encrypt
            to_encrypt = input(">>> string to encrypt: ")
            if len(to_encrypt) == 0:
                print("Nothing to encrypt!")
                continue
            encrypted = ""
        elif option == 2:  # input key
            key = input(">>> key to encrypt with: ")
            if len(key) == 0:
                print("Nothing to encrypt with!")
                continue
            encrypted = ""
        elif option == 3:  # encrypt
            encrypted = ""
            if key == "" or to_encrypt == "":
                print("Set a key and the string to encrypt!")
                continue
            for idx in range(len(to_encrypt)):
                row = ord(to_encrypt[idx]) - zero_offset
                col = ord(key[idx % len(key)]) - zero_offset
                encrypted += shift_string(alphabet, row)[col]
            print("encrypted: ")
            print(encrypted)
        elif option == 4:  # decrypt
            if encrypted == "": # check if something is encrypted
                print("Nothing is encrypted yet!")
                continue
            decrypted = ""
            for idx in range(len(encrypted)):
                # note: because the matrix is symmetrical, row/column do not matter
                key_char = key[idx % len(key)]
                col_idx = alphabet.index(key_char)
                row_idx = shift_string(alphabet, col_idx).index(encrypted[idx])
                decrypted += alphabet[row_idx]
            print("decrypted:")
            print(decrypted)

        elif option == 5:
            print("tabula")
            print("\n".join([" ".join(list(shift_string(alphabet, row))) for row in range(len(alphabet))]))
        elif option == 6:
            break


if __name__ == "__main__":
    main()
