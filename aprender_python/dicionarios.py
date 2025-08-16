#Dicionarios
tempos = {
    "via A": 10,
    "via B": 20,
    "via C": 30
}

print(tempos["via C"])
for via in tempos:
    print(via," = ",tempos[via]," segundos.")