numero_funcionario = int(input("Insira o seu numero de funcionario: "))
horas_trabalhadas = int(input("Insira as horas trabalhadas: "))
valor_por_hora = int(input("Insira o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"O salário do funcionário {numero_funcionario} é igual a R$ {salario} reais")