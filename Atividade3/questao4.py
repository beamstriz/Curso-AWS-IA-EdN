# Solicita os dados ao usuário
temperatura = float(input("Digite a temperatura: "))
unidadeOrigial = input("Está em qual unidade? digite C, F OU K: ").upper()
unidadeConvertida = input("Digite a unidade que queres converter C, F ou K: ").upper()

def c_para_f(c):
    return (c *9/5) + 32

def f_para_c(f):
    return (f - 32)*5/9

def c_para_k(c):
   return c + 273.15

def k_para_c(k):
    return k - 273.15

def f_para_k(f):
    return c_para_k(f_para_c(f))

def k_para_f(k):
    return c_para_f(k_para_c(k))

if unidadeOrigial == 'C' and unidadeConvertida == 'F':
    resultado = c_para_f(temperatura)
elif unidadeOrigial == 'F' and unidadeConvertida == 'C':
    resultado = f_para_c(temperatura)
elif unidadeOrigial == 'C' and unidadeConvertida == 'K':
    resultado = c_para_k(temperatura)
elif unidadeOrigial == 'K' and unidadeConvertida == 'C':
    resultado = k_para_c(temperatura)
elif unidadeOrigial == 'F' and unidadeConvertida == 'K':
    resultado = f_para_k(temperatura)
elif unidadeOrigial == 'K' and unidadeConvertida == 'F':
    resultado = k_para_f(temperatura)
elif unidadeOrigial == unidade_destino:
    resultado = temperatura

print(f"{temperatura}{unidadeOrigial} = {resultado:.2f}{unidadeConvertida}")