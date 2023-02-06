key = "56921" #ключ
alfavit = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" #алфавит для логина и пароля


def encrypt(string, key, alfavit): #функция шифрования
    j = 0
    encrypt_string = ""
    for i in range(len(string) - len(key)): #увеличиваем ключ под длину сообщения
        key += key[i]
    for symbol in string: #проходим по каждому символу в строке
        if symbol in alfavit: #ищем символ в алфавите
            encrypt_string += alfavit[(alfavit.find(symbol) + int(key[j])) % len(alfavit)] #находим индекс символа в алфавите, смещаем его на значение подключа вправо и записываем новый символ к зашифрованной строке
            j += 1 #переходим к следующему значению подключа
        else:
            encrypt_string += symbol
    return encrypt_string

