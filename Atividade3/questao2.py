idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Você ainda é uma criança")

elif idade >= 13 and idade <= 17:
    print("Você é considerado um adolescente")

elif idade>= 18 and idade <= 59:
    print("Você é considerado um adulto")

elif idade>= 60:
    print("Você é considerado um idoso")
