def aumentar(preço=0, taxa=0, formato=False):
    """

    :param preço: Valor digitado pelo usuário.
    :param taxa: Valor em porcentagem acrescido ou retirado.
    :param formato: Formatação de valor monetário padrão brasileiro.
    :return: Restorna a operação
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:>.2f}'.replace(".", ",")
