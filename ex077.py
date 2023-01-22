palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'praticar', 'trabalhar', 'programador', 'futuro', 'estudar',
            'tupla', 'inicio')
for p in palavras:
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos a vogal - ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
