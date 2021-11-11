'''
@author: habi2
'''
import random

LAN_NUM_SOLDIERS = 10_000
BAR_NUM_SOLDIERS = 10_000

pwr_lan = []
pwr_bar = []
pwr_groups_lan = []
pwr_groups_bar = [[], [], [], [], [], [], [], [], []]

for _ in range (BAR_NUM_SOLDIERS):
    pwr_bar.append(random.randrange(10, 100)) 

#Generamos la clasfificacion de poderes dentro de la lista:
"""for i in range(LAN_Npwr_barUM_SOLDIERS):
    if i == (1_000 or 2_000 or 3_000 or 4_000):"""

"""
Para los [], mejor 
for _ in range(9):
    list.append([])
y luego ir generando los numeros segun avanza el for en vez de generar una lista primero y luego
ir comprobando.
Otra forma de asignar la columna es hacer // 10 y asiganar el numero entero a la fila que le corresponda


"""

for i in range(BAR_NUM_SOLDIERS):
    if pwr_bar[i] >= 90:
        pwr_groups_bar[0].append(pwr_bar[i])
    elif pwr_bar[i] >= 80:
        pwr_groups_bar[1].append(pwr_bar[i])
    elif pwr_bar[i] >= 70:
        pwr_groups_bar[2].append(pwr_bar[i])
    elif pwr_bar[i] >= 60:
        pwr_groups_bar[3].append(pwr_bar[i])
    elif pwr_bar[i] >= 50:
        pwr_groups_bar[4].append(pwr_bar[i])
    elif pwr_bar[i] >= 40:
        pwr_groups_bar[5].append(pwr_bar[i])
    elif pwr_bar[i] >= 30:
        pwr_groups_bar[6].append(pwr_bar[i])
    elif pwr_bar[i] >= 20:
        pwr_groups_bar[7].append(pwr_bar[i])
    elif pwr_bar[i] >= 10:
        pwr_groups_bar[8].append(pwr_bar[i])
    elif pwr_bar[i] >= 1:
        pwr_groups_bar[9].append(pwr_bar[i])
    

print(pwr_groups_bar)