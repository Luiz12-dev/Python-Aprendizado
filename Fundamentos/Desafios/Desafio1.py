hps_inimigos = [0,150,0,32,0,85]

vivos = []
derrotados = []

for posicao in hps_inimigos:
    if posicao > 0:
        vivos.append(posicao)
    else:
        derrotados.append(posicao)

print("vivos: ", vivos)
print("derrotados: ", derrotados)

"""
O Problema:
Dada a lista hps_inimigos = [0, 150, 0, 32, 0, 85], 
crie duas novas listas vazias: vivos e derrotados. Use um loop para percorrer a lista original. Se o HP for maior que zero, 
adicione à lista de vivos. Caso contrário, adicione à lista de derrotados. 
No final, imprima as duas listas.
"""