def identificar_animal(caracteristica1, caracteristica2, caracteristica3):
    arvore_decisao = {
        "vertebrado": {
            "ave": {"carnivoro": "aguia", "onivoro": "pomba"},
            "mamifero": {"onivoro": "homem", "herbivoro": "vaca"},
        },
        "invertebrado": {
            "inseto": {"hematofago": "pulga", "herbivoro": "lagarta"},
            "anelideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"},
        }
    }

    try:
        animal = arvore_decisao[caracteristica1][caracteristica2][caracteristica3]
        return animal
    except KeyError:
        return "Animal não encontrado na base de dados."

caracteristica1 = str(input())
caracteristica2 = str(input())
caracteristica3 = str(input())


resultado = identificar_animal(caracteristica1, caracteristica2, caracteristica3)
print(resultado)
