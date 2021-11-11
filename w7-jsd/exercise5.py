'''
@title: exercise5
@author: habi2
@date: 24/10/2021

Create three dictionaries: maria, peter, and mike. Give each dictionary the keys ’name’,
’weeklyExercises’ and ’weeklyTests. Have the ’name’ key be the name of the student
(that is, maria’s name should be ’Maria’ and so on). The other keys should be an empty list.
Print the dictionaries on the screen. Next populate each list with 10 random numbers in the
range 0 to 10. For each of the dictionaries create a new key named exam and fill it with a
random value in the range 0 to 10.
'''
import random
a, b, c, d, e, f = [],[],[],[],[],[] 

maria = {'name': 'Maria', 'weeklyExercises': a,'weeklyTests': d}
peter = {'name': 'Peter', 'weeklyExercises': b,'weeklyTests': e} 
mike = {'name': 'Mike', 'weeklyExercises': c,'weeklyTests': f}

print(maria,peter,mike, sep='\n')

for _ in range(10):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))
    c.append(random.randint(0, 10))
    d.append(random.randint(0, 10))
    e.append(random.randint(0, 10))
    f.append(random.randint(0, 10))
maria['exam'] = random.randint(0, 10)
peter['exam'] = random.randint(0, 10)
mike['exam'] = random.randint(0, 10)
    
print(maria,peter,mike, sep='\n')

