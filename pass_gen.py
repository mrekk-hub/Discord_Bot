from random import randrange as r


def code(length: int) -> str:
    s = [0] * length
    storage = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if (i + 1) % 4 == 0 and i != len(s) - 1:
            s[i] = '-'
        else:
            s[i] = storage[r(0, 62)]
    return ''.join(s)


def code_s(length: int) -> str:
    s = [0] * length
    storage = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
    symbols = '%*)?@#$~'
    for i in range(len(s)):
        if (i + 1) % 4 == 0 and i != len(s) - 1:
            s[i] = symbols[r(7)]
        else:
            s[i] = storage[r(0, 62)]
    return ''.join(s)


def verbal(length: int) -> str:
    s = []
    with open(r'C:\Users\MAX-Ryzen\Desktop\pythonProjectBotFinal\ENRUS.TXT') as file:
        content = file.readlines()
        for i in range(length):
            a = r(10, 102000, 2)
            s.append(content[a][:content[a].find(' ')])
            s.append('-')
        s.append(str(r(100)))
        return ''.join(s)
