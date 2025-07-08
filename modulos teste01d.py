from random import choice, sample
n1 = input('digite aqui o nome: ')
n2 = input('digite o nome do segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
myTable = [n1, n2, n3, n4]
#print(f'o nome selecionado eh {choice(myTable)}')
print(f'a ordem dos selecionados sera {sample(myTable, k = 4)}')