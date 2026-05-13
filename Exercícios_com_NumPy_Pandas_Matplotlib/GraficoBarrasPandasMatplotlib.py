import pandas as pd
import matplotlib.pyplot as plt
import random

dados = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'vendas': [1200, 1500, 1700, 1600, 1800, 2000]
}

df = pd.DataFrame(dados)

# Função para gerar cores aleatórias
def cor_aleatoria():
    cores = ['red', 'blue', 'green', 'orange', 'purple', 'pink']
    return random.choice(cores)

# Gráfico
plt.bar(df['mes'], df['vendas'], color='red')

plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas')

plt.show()
