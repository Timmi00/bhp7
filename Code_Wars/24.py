def justify(text, width):
    n = text.split(' ')
    res = ''
    fulres = ''
    i = 0
    while n:
        if len(res) + len(n[0]) < width:
            i = len(n[0])
            if len(res) != 0:
                res += ' '
            res += n.pop(0)
            if len(n) == 0:
                fulres += res
        elif len(res) + len(n[0]) == width - 1:
            res += ' '
            res += n.pop(0)
            fulres += res + '\n'
            res = ''
        else:
            y = 0
            while len(res) != width:
                y = res.find(' ',y + 1)
                print(res[y])
                res = res[0:y] + ' ' + res[y:]
                y += 1
            fulres += res + '\n'
            res = ''
    return fulres


print(justify('123 42222225 6 9 999 1 3131 999 1212 991 1121212122 313 11 331 113 4232 1 1 122121212123 45 6 9 999 1 3131 999 12212112 9921212191 1212121212 313 11 331 1313 4232 1 1 123 45 6 9 99999 1 3131 9999 1212 9991 12 313 11 331 1313 4232 1 1 123 45 6 9 99999 1 3131 9999 1212 9991 12 313 11 331 1313 4232 1 1 123 45 6 9 99999 1 3131 9999 1212 9991 12 313 11 331 1313 4232 1 1 123 45 6 9 99999 1 3131 9999 1212 9991 12 313 11 331 1313 4232 1 1 123 45 6 9 99999 1 3131 9999 1212 9991 12 313 11 331 1313 4232 1 1', 15))
