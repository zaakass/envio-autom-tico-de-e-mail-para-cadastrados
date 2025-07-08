q = float(input("diga uma medida em metros: "))
print(f'A medida {q}m é:\n'
      f'{q / 1000:.2f}km \n{q / 100:.2f}hm\n'
      f'{q / 10:.2f}dam\n{q * 10}dm\n'
      f'{q * 100}cm \n{q * 1000}mm')