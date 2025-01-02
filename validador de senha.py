import re

def validar_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    # Verifica se a senha contém letras maiúsculas e minúsculas
    if not re.search(r'[A-Z]', senha):
        return "A senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r'[a-z]', senha):
        return "A senha deve conter pelo menos uma letra minúscula."

    # Verifica se a senha contém pelo menos um número
    if not re.search(r'[0-9]', senha):
        return "A senha deve conter pelo menos um número."

    return "Senha válida."

# Testar a função
senha = input("Digite a senha para validar: ")
resultado = validar_senha(senha)
print(resultado)
