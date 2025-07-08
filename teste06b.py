value = float(input("escolhha um numero inteiro: "))
#print("o dobro do seu numero eh {}, o triplo eh {}, \nE a raiz quadrada eh {:.2f}".format(value * 2, value * 3, value ** (1/2)))
print(f"o dobro do seu numero eh {value * 2}, o triplo eh {value * 3}, \nE a raiz quadrada eh {pow(value, (1/2)):.2f}")