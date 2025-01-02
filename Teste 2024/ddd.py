ddd = int(input())

def destination(ddd):
    cod_cidade = {
        61:"Brasilia",
        71:"Salvador",
        11:"São Paulo",
        21:"Rio de Janeiro",
        32:"Juiz de Fora",
        19:"Campinas",
        27:"Vitoria",
        31:"Belo Horizonte"
    }

    try:
        cidade = cod_cidade[ddd]
        return cidade
    except KeyError:
        return "DDD nao cadastrado"

resultado = destination(ddd)
print(resultado)
