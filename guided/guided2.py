"""
@title: guided2.py
@author: Javier Sanz Diaz 
"""

climate = input('Is it day or night?(d/n)').lower()
num_sol = int(input('Number of soldiers?'))
num_eng = int(input('Number of siege engines?'))
poison = input('Do we want to use poison?(y/n)').lower()
rain = input('Is it rainy outside?(y/n)').lower()

satisfied = False
if (climate == 'n' 
        and rain == 'n' 
        and num_sol >= 500 
        and num_eng >= 50):
    print('The recommended strategy is A: “Silent attack”.')
    satisfied = 1

if (climate == 'd' 
        and num_sol >= 10000):
    print('The recommended strategy is B: “Crossfire”.')
    satisfied = 1

if (climate == 'n' 
        and num_sol >= 1 
        and poison == 'y'):
    print('The recommended strategy is C: “Kill the King”.')
    satisfied = 1

if not satisfied:
    satA = satB = satC = ''
    unsatA = unsatB  = unsatC = ''

    #The ones from A:
    #climate
    if climate == 'n':
        satA += 'night, '
    else:
        unsatA += 'night, '
    #rain
    if rain == 'n':
        satA += 'rain, '
    else:
        unsatA += 'rain, '
    #num_sol
    if num_sol < 500:
        satA += 'more than 500 soldiers, '
    else:
        unsatA += 'more than 500 soldiers, '
    #num_eng
    if num_eng < 50:
        satA += 'more than 50 siege engines, '
    else:
        unsatA += 'more than 50 siege engines, '
    
    #The ones from B:
    #climate
    if climate == 'd':
        satB += 'day, '
    else:
        unsatB += 'day, '
    #num_sol
    if num_sol < 1000:
        satB += 'more than 1000 soldiers, '
    else:
        unsatB += 'more than 10000 soldiers, '
    
    #The ones from C:
    #climate
    if climate == 'n':
        satC += 'night, '
    else:
        unsatC += 'night, '
    #num_sol
    if num_sol >= 1:
        satC += 'more than 1 soldiers, '
    else:
        unsatC += 'more than 1 soldiers, '
    #poison
    if poison == 'y':
        satC += 'poison, '
    else:
        unsatC += 'poison, '
    
    print(f'''None of the three strategies is satisfied completely but I'll tell
    you what you satisfy for each of them right now so you can take a decision:
    
    Strategy A:
    Satisfied: {satA}\b\b
    Unsatisfied: {unsatA}\b\b

    Strategy B:
    Satisfied: {satB}\b\b
    Unsatisfied: {unsatB}\b\b

    Strategy C:
    Satisfied: {satC}\b\b
    Unsatisfied: {unsatC}\b\b
    ''')
