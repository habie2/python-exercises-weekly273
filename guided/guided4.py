"""
@title: guided4.
@author: Javier Sanz Diaz
@date: 14 Oct 2021
"""
from math import atan
import random

ATTACKER = 10_000
DEFENDER = 3_200
pwr_attacker = []
pwr_defender = []

for _ in range(ATTACKER):
    pwr_attacker.append(random.randrange(10, 50))
for _ in range(DEFENDER):
    pwr_defender.append(random.randrange(10, 50) + 25)

while (len(pwr_attacker) and len(pwr_defender)) != 0:
    attacker = 0
    defender = 0
    if pwr_defender[defender] >= pwr_attacker[attacker]:
        pwr_defender[defender] -= pwr_attacker[attacker]/3
        del(pwr_attacker[attacker])
        defender += 1
    else:
        pwr_attacker[attacker] -= pwr_defender[defender]/3
        del(pwr_defender[defender])
        attacker += 1
print(len(pwr_defender))
print(len(pwr_attacker))
#if pwr_defender[random.randrange(len(pwr_defender))] >= pwr_attacker[random.randrange(len(pwr_attacker))]: