import json

pessoa = {
    "nome": "João",
    "idade": 28,
    "cidade": "Fortaleza"
}

with open("pessoa.json", "w", encoding="utf-8") as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

with open("pessoa.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print("Dados lidos do JSON:")
    print(dados)
