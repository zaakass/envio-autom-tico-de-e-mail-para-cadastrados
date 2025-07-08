import numpy as np
import matplotlib.pyplot as plt

# Define a função da questão B
def f(x):
    return -x**2 + 10*x + 5

# Configuração do intervalo de x para visualizar a parábola
x = np.linspace(-2, 12, 400)  # Intervalo ampliado para capturar as raízes
y = f(x)

# Cálculo das raízes (onde f(x) = 0)
delta = 10**2 - 4*(-1)*5
raiz1 = (-10 + np.sqrt(delta)) / (2*(-1))
raiz2 = (-10 - np.sqrt(delta)) / (2*(-1))

# Cálculo do vértice
vertice_x = -10 / (2*(-1))  # Fórmula: -b/(2a)
vertice_y = f(vertice_x)

# Configurações do gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = -x^2 + 10x + 5$', color='purple', linewidth=2)

# Linhas de eixos e grid
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

# Destacar raízes e vértice
plt.scatter([raiz1, raiz2], [0, 0], color='red', s=100, label=f'Raízes: x≈{raiz1:.2f}, x≈{raiz2:.2f}')
plt.scatter(vertice_x, vertice_y, color='gold', s=100, label=f'Vértice: ({vertice_x:.2f}, {vertice_y:.2f})')

# Ajustes estéticos
plt.title('Gráfico de $f(x) = -x^2 + 10x + 5$ (Questão B)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()