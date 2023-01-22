largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
m2 = largura * altura
t = m2 / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(largura, altura, m2, t))
