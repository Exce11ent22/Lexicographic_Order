alphabet = 'abcdefghijklmnopqrstuvwxyz'


def code(word):
    global alphabet
    l = len(alphabet)
    result = 0
    for i, char in enumerate(word[::-1]):
        n = alphabet.index(char) + 1
        result += n * l ** i
    return result


def decode(n):
    global alphabet
    l = len(alphabet)
    result = ''
    while n > 0:
        if n % l == 0:
            result = alphabet[l - 1] + result
            n = (n // l) - 1
        else:
            i = n % l
            n //= l
            result = alphabet[i - 1] + result
    return result


def main():
    while True:
        print(code(input('Введите слово: ')))
        print(decode(int(input('Введите число: '))))


if __name__ == '__main__':
    main()
