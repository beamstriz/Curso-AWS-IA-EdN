preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print(f"Preço final: R$ {preco_final:.2f}")