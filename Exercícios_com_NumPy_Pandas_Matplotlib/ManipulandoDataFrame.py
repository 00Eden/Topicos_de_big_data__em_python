import pandas as pd

dados = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Eva'],
    'nota_prova1': [6.5, 7.0, 8.0, 5.5, 9.0],
    'nota_prova2': [7.5, 6.0, 8.5, 6.0, 8.0]
}

df = pd.DataFrame(dados)

# 2.1 Média
df['media'] = (df['nota_prova1'] + df['nota_prova2']) / 2

# 2.2 Aprovado
df['aprovado'] = df['media'] >= 7

# 2.3 Apenas aprovados
aprovados = df[df['aprovado'] == True]

print(df)
print("\nAlunos aprovados:")
print(aprovados)
