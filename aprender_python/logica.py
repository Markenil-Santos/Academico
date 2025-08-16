#Uso de logica de controle
tempos = {
    "via A": 10,
    "via B": 20,
    "via C": 30
}
for via in tempos:
    print(via," = ",tempos[via]," segundos.")

for vias in tempos:
    if tempos[vias] < 12:
        tempos[vias] += 5
        
for via in tempos:
    print(via," = ",tempos[via]," segundos.")

      