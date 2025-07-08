from  math import  sqrt, pow

catA = float(input('escreva um numero para o cateto adjacente: '))
catO = float(input('escreva um numero para o cateto oposto: '))
h = sqrt(pow(catA, 2) + pow(catO, 2))
print(f'a hipotenusa desses dois catetos eh {h:.2f}')