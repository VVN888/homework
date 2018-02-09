# 1-я функция
def dec2bin(number):
    x = number
    n = "" if x > 0 else "0"
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    return (n)

    dlina = len(n)
    chislo_dec = 0
    for i in range(0, dlina):
        chislo_dec = chislo_dec+int(n[i])*(2**(dlina-i-1))

# print(dec2bin(250)))
# print(dec2bin(250))


# 2-я функция
def dec2oct(number):
    x = number
    n = "" if x > 0 else "0"
    while x > 0:
        y = str(x % 8)
        n = y + n
        x = int(x / 8)
    return (n)

# print(dec2oct(250)))
# print(dec2oct(250))


# 3-я функция
def dec2hex(number):
    n = int(number)
    d = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
     10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    q = n
    result = ""
    while q != 0:
        r = q % 16
        q = q // 16
        result += d[r]
        result = ''.join(reversed(result))
    return (str(result))

 # print(type(dec2hex(250)))
 # print(dec2hex(250))


# 4-я функция
def bin2dec(number):
    dlina = len(number)
    chislo_dec = 0
    for i in range(0, dlina):
        chislo_dec = chislo_dec+int(number[i])*(2**(dlina-i-1))
    return chislo_dec

# print(type(bin2dec('1010011010')))
# print(bin2dec('1010011010'))


# 5-я функция
def oct2dec(number):
    dlina = len(number)
    chislo_dec = 0
    for i in range(0, dlina):
        chislo_dec = chislo_dec+int(number[i])*(8**(dlina-i-1))
    return chislo_dec

# print(type(oct2dec('755')))
# print(oct2dec('755'))


# 6-я функция
def hex2dec(number):
    n = str(number)
    q = len (n)
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
     'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,
     'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    i = 0
    g = []
    chislo_dec = 0
    while i != q:
        h = (n[i])
        result = d[h]
        g.append(result)
        chislo_dec = chislo_dec+int((g[i])*(16**(q-i-1)))
        i += 1
    return (chislo_dec)

 # print(type(hex2dec('abcdef')))
 # print(hex2dec('abcdef'))
