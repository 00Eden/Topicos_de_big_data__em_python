alunos = {
    "Ana": [9, 8, 10],
    "Bruno": [7, 6, 8],
    "Carla": [10, 9, 9],
    "Diego": [5, 6, 7],
    "Eva": [8, 9, 9],
    "Felipe": [6, 5, 7],
    "Giovana": [10, 10, 9],
    "Henrique": [7, 8, 8],
    "Isabela": [9, 9, 8],
    "João": [4, 5, 6]
}

# Criando arquivo
with open("aprovados.txt", "w", encoding="utf-8") as arquivo:

    for nome, notas in alunos.items():

        media = sum(notas) / 3

        if media > 8:
            mensagem = f"{nome} - Parabéns, você foi aprovado em Python.\n"
            arquivo.write(mensagem)

# Lendo arquivo
with open("aprovados.txt", "r", encoding="utf-8") as arquivo:

    conteudo = arquivo.read()

print(conteudo)
