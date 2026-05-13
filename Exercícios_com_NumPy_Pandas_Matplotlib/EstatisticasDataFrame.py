import pandas as pd

dados_vendas = {
    'produto': ['Notebook Dell Inspiron', 'Mouse Logitech M170', 'Teclado Mecânico Redragon', 'Monitor LG 24"', 'Headset HyperX Cloud', 'Notebook Dell Inspiron', 'Mouse Logitech M170', 'Smartphone Samsung Galaxy A54', 'Smartphone Samsung Galaxy A54', 'Cadeira Gamer ThunderX3', 'Webcam Logitech C920', 'Monitor LG 24"', 'Teclado Mecânico Redragon', 'Headset HyperX Cloud', 'Cadeira Gamer ThunderX3', 'SSD Kingston 480GB', 'SSD Kingston 480GB', 'HD Externo Seagate 1TB', 'HD Externo Seagate 1TB', 'Webcam Logitech C920'],
    
    'categoria': ['Informática', 'Periféricos', 'Periféricos', 'Informática', 'Periféricos', 'Informática', 'Periféricos', 'Telefonia', 'Telefonia', 'Móveis', 'Periféricos', 'Informática', 'Periféricos', 'Periféricos', 'Móveis', 'Armazenamento', 'Armazenamento', 'Armazenamento', 'Armazenamento', 'Periféricos'],
    
    'valor': [3500, 80, 250, 900, 400, 3400, 75, 1800, 1750, 1200, 350, 880, 260, 390, 1150, 220, 210, 350, 340, 360]
}

df = pd.DataFrame(dados_vendas)

# 3.1 Quantidade e total por produto
resumo = df.groupby('produto').agg({
    'valor': ['count', 'sum']
})

print("Resumo de vendas:")
print(resumo)

# 3.2 Produto com maior média de venda
media_produtos = df.groupby('produto')['valor'].mean()

produto_maior_media = media_produtos.idxmax()
valor_maior_media = media_produtos.max()

print("\nProduto com maior média de venda:")
print(produto_maior_media)
print(valor_maior_media)

# 3.3 Valor acumulado
df['valor_acumulado'] = df['valor'].cumsum()

print("\nDataFrame com valor acumulado:")
print(df)
