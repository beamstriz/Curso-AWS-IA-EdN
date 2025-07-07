def eh_palindromo(texto: str) -> str:
    texto_limpo = ''.join(c for c in texto.lower() if c.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"