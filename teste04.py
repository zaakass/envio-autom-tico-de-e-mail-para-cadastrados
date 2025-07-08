r1 = int(input('escolha um numero: '))
r2 = int(input('escolha outro: '))
s = r1 + r2
su = r1 - r2
m = r1 * r2
d = r1 / r2
di = r1 // r2
ml = r1 % r2
e = r1 ** r2
print('A soma entre {} e {} é {},'.format(s, r2, s), end=' ')
print('a subtração é {},'.format(su), end=' ')
print('a multiplicação é {},'.format(m), end=' ')
print('a divisão é {},'.format(d), end=' ')
print('a divisão inteira é {},'.format(di), end=' ')
print('o módulo é {} e a potência é {}.'.format(ml, e))
