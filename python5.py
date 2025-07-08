def even_or_odd(numero):
     return "o numero eh par" if numero % 2==0 else "o numero eh impar"
num = int(input("digite um numero: "))
print(even_or_odd(num))