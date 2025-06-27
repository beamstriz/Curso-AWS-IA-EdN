ano = int(input("Digite o ano: "))

if ano%4 == 0 and ano%100!=0:
    print("É ano bissexto") 
else: 
    print(f"{ano} não é bissexto")