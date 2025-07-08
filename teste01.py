import time

name_number1 = input(
    "escolha um numero para que eu some com o proximo que voce escolher: "
)
time.sleep(1)
print("obrigado!")
time.sleep(1)
print("agora, pedirei para voce escolher o proximo numero...")
time.sleep(2)
name_number2 = input("escolha o novo numero para a soma ser realizada: ")
print("ok! agora, espere um momento...")
time.sleep(3)
print(f"a soma dos seus numeros foi de: ",name_number1 + name_number2, "!")
