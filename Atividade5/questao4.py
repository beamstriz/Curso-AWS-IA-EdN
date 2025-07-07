from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    hoje = date.today()
    idade = hoje.year - ano_nascimento
    return idade * 365 + (idade // 4) 