import requests

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    if "erro" not in dados:
        print("Logradouro:", dados.get("logradouro", "N/A"))
        print("Bairro:", dados.get("bairro", "N/A"))
        print("Cidade:", dados.get("localidade", "N/A"))
        print("Estado:", dados.get("uf", "N/A"))
    else:
        print("CEP não encontrado.")
else:
    print("Erro ao acessar a API.")
