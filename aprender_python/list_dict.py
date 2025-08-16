#Dicionarios e manipulação com laço
dado = {"via A": 12, "via B": 8, "via C": 3}
def ajusta_tempo(dado_dados):
    tempo_calc ={}
    
    for vias in dado_dados:
        tempo_atual = dado_dados[vias]
        if tempo_atual > 10:
            tempo_calc[vias] = 30
            
        elif tempo_atual >= 5 and tempo_atual <=10:
            tempo_calc[vias] = 20
            
        elif tempo_atual < 5:
            tempo_calc[vias] = 10
            
    return tempo_calc      
            
        
    
    
    
print(ajusta_tempo(dado))
