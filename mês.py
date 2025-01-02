data = int(input())

def ano(data):

    cod_mes = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    try:
        mes = cod_mes[data]
        return mes
    except KeyError:
        return "Mês inexistente."

resultado = ano(data)
print(resultado)
