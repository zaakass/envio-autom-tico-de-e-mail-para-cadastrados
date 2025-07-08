import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 10))
plt.title("MATRIZ DE EISENHOWER - JORGE CORRAL", fontsize=18, pad=20, weight='bold')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.axis('off')

# Linhas divisorias mais espessas
plt.axvline(5, color='gray', linewidth=3, alpha=0.7)
plt.axhline(5, color='gray', linewidth=3, alpha=0.7)

# Cores de fundo para os quadrantes
plt.gca().add_patch(plt.Rectangle((0, 5), 5, 5, color='#FFDDDD', alpha=0.3))
plt.gca().add_patch(plt.Rectangle((5, 5), 5, 5, color='#DDFFDD', alpha=0.3))
plt.gca().add_patch(plt.Rectangle((0, 0), 5, 5, color='#FFFFDD', alpha=0.3))
plt.gca().add_patch(plt.Rectangle((5, 0), 5, 5, color='#DDDDFF', alpha=0.3))

# Títulos dos quadrantes em negrito
plt.text(2.5, 8.7, "URGENTE E IMPORTANTE\n(FAZER AGORA)", 
         fontsize=14, ha='center', weight='bold', color='darkred')
plt.text(7.5, 8.7, "IMPORTANTE MAS NÃO URGENTE\n(AGENDAR)", 
         fontsize=14, ha='center', weight='bold', color='darkgreen')
plt.text(2.5, 3.7, "URGENTE MAS NÃO IMPORTANTE\n(DELEGAR)", 
         fontsize=14, ha='center', weight='bold', color='darkorange')
plt.text(7.5, 3.7, "NÃO URGENTE E NÃO IMPORTANTE\n(ELIMINAR OU POSTERGAR)", 
         fontsize=14, ha='center', weight='bold', color='purple')

# Tópicos por quadrante
urgente_importante = [
    "• Relatar BUG",
    "• Bug após entrar (volta à home)",
    "• Botão perfil não existe"
]

importante_nao_urgente = [
    "• Explicação e monitoramento de rating",
    "• Ranking (respostas/posts)",
    "• Separar por tópicos",
    "• Acesso a região"
]

nao_importante_urgente = [
    "Nenhum tópico"
]

nao_urgente_nao_importante = [
    "• Chat em tempo real (VIP)",
    "• Aplicativo",
    "• Pop-up de entrar"
]

# Função para plotar os itens centralizados
def plot_items(items, x, y, spacing=0.8, fontsize=12):
    for i, item in enumerate(items):
        plt.text(x, y - i*spacing, item, 
                 fontsize=fontsize, 
                 ha='center',
                 va='center',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=8))

# Posicionamento dos tópicos - centralizados nos quadrantes
plot_items(urgente_importante, 2.5, 7.0)
plot_items(importante_nao_urgente, 7.5, 7.0)
plot_items(nao_importante_urgente, 2.5, 2.0, fontsize=11)
plot_items(nao_urgente_nao_importante, 7.5, 2.0)

# Legenda de priorização
plt.figtext(0.5, 0.01, 
            "Priorização baseada no estado atual do site (não funcional)", 
            ha="center", fontsize=10, style="italic")

plt.tight_layout(pad=3.0)
plt.savefig('matriz_eisenhower_melhorada.png', dpi=120, bbox_inches='tight')
plt.show()