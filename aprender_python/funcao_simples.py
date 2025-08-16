#Função simples
def tempo_verde(carros):
    if carros > 10:
        return 30
    elif carros >= 5 and carros <=10:
        return 20
    elif carros < 5:
        return 10

print(tempo_verde(19))