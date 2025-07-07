import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Clara", 35, "Belo Horizonte"]
]

with open("pessoas.csv", "w", newline='', encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)

print("Arquivo 'pessoas.csv' criado com sucesso.")
