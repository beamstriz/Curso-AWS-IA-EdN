# Lê os dados de entrada
nome = input("Nome do vendedor: ")
salariofixo = float(input("Salário fixo: "))
vendaS = float(input("Total de vendas no mes: "))

comissao = vendas * 0.15

totalReceber = salarioFixo + comissao

print(f"TOTAL = R$ {totalReceber:.2f}")
