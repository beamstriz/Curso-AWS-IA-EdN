peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em m: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")