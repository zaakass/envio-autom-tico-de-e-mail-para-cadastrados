from math import sin, cos, tan, radians
ang = float(input('adicione aqui um angulo: '))
ang_rad = radians(ang)
print(f'o seno do angulo digitado eh {sin(ang_rad):.2f}\no cosseno eh {cos(ang_rad):.2f}\ne a tangente eh {tan(ang_rad):.2f}.')