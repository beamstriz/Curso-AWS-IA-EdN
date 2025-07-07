import requests

moeda = input("Digite o código da moeda como USD, EUR...: ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave in dados:
        info = dados[chave]
        print("Moeda:", info['name'])
        print("Valor atual:", info['bid'])
        print("Valor máximo:", info['high'])
        print("Valor mínimo:", info['low'])
        print("Última atualização:", info['create_date'])
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao acessar a API.")
