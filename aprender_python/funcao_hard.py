#Função com multiplos parâmetros
def calcula_tempo(via, carros):
    if carros > 10:
        return f"{via}: 30 segundos de verde"
    elif carros >= 5 and carros <=10:
        return f"{via}: 20 segundos de verde"
    elif carros < 5:
        return f"{via}: 10 segundos de verde"
    
    
print(calcula_tempo("via A", 12))
print(calcula_tempo("via B", 4))