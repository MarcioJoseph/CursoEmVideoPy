#a = float(input("digita ai: "))
#b = float(input("digita ai: "))
#c = float(input("digita ai: "))
#pa = 2
#pb = 3
#pc = 5

#media = (a * pa + b * pb + c * pc) / (pa + pb + pc)

#print(f"MEDIA = {media:.1f}")


#nome = str(input("nome: "))
#salfix = float(input("salario: "))
#vendas = float(input("Vendas: "))
#comicao = vendas * 15 / 100
#total = comicao + salfix

#print(f"TOTAL = R$ {total:.2f}")

#peca1 = int(input("peca1: "))
#qtde_peca1 = int(input("qtde: "))
#valor_peca1 = float(input("valor: "))

#peca2 = int(input("peca2: "))
#qtde_peca2 = int(input("qtde: "))
#valor_peca2 = float(input("valor: "))

#venda_peca1 = qtde_peca1 * valor_peca1
#venda_peca2 = qtde_peca2 * valor_peca2

#total = venda_peca1 + venda_peca2

#print(f"VALOR A PAGAR: R$ {total:.2f}")

# Leitura dos dados da peça 1
codigo1, numero_pecas1, valor_unitario1 = input().split()
codigo1 = int(codigo1)
numero_pecas1 = int(numero_pecas1)
valor_unitario1 = float(valor_unitario1)

# Leitura dos dados da peça 2
codigo2, numero_pecas2, valor_unitario2 = input().split()
codigo2 = int(codigo2)
numero_pecas2 = int(numero_pecas2)
valor_unitario2 = float(valor_unitario2)

# Cálculo do valor total a ser pago
valor_total = (numero_pecas1 * valor_unitario1) + (numero_pecas2 * valor_unitario2)

# Impressão do resultado
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
