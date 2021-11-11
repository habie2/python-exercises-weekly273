'''
@title: exercise6
@author: habi2
@date: 24/10/2021

Create a list called students with the dictionaries of Exercise 1. For each element in the list:
a. Calculate the average of the weekly exercises and weekly tests, their maximum and their
minimum and add them as a 3-elements list at the last position of each list.
b. Add to each dictionary a new key called mark which contains the mark of the student
calculated as follows: WeeklyExercises are 10%, weeklyTests are 30%, and exam is
60%.
c. Add a new key called letterGrade whose value is:
    · ’A’, if the score is 9 or above;
    · ’B’ if the score is 8 or above;
    · ’C’, if the score is 7 or above;
    · ’D’, if the score is 6 or above.
    · ‘E’ if the score is 5 or above.
    · ‘F’ in any other case.
d. Print each element in students, one key per line.
e. Calculate and print the average mark of the class (average mark of the students)
'''
import random
avg_marks = 0
def paso_a(dicName):
    min_persona = min(dicName['weeklyExercises'])
    max_persona = max(dicName['weeklyExercises'])
    avg_persona_ex = sum(dicName['weeklyExercises']) / len(dicName['weeklyExercises'])
    dicName['weeklyExercises'].append([])
    dicName['weeklyExercises'][10].append(min_persona)
    dicName['weeklyExercises'][10].append(max_persona)
    dicName['weeklyExercises'][10].append(avg_persona_ex)
    min_persona = min(dicName['weeklyTests'])
    max_persona = max(dicName['weeklyTests'])
    avg_persona_test = sum(dicName['weeklyTests']) / len(dicName['weeklyTests'])
    dicName['weeklyTests'].append([])
    dicName['weeklyTests'][10].append(min_persona)
    dicName['weeklyTests'][10].append(max_persona)
    dicName['weeklyTests'][10].append(avg_persona_test)
    dicName['exam'] = random.randint(0, 10)
    dicName['mark'] = avg_persona_ex * .1 + avg_persona_test * .3 + dicName['exam'] * .6
    if dicName['mark'] >= 9:
        dicName['letterGrade'] = 'A'
    elif dicName['mark'] >= 8:
        dicName['letterGrade'] = 'B'
    elif dicName['mark'] >= 7:
        dicName['letterGrade'] = 'C'
    elif dicName['mark'] >= 6:
        dicName['letterGrade'] = 'D'
    elif dicName['mark'] >= 5:
        dicName['letterGrade'] = 'E'
    else:
        dicName['letterGrade'] = 'F'
        	


a, b, c, d, e, f = [],[],[],[],[],[] 
maria = {'name': 'Maria', 'weeklyExercises': a,'weeklyTests': d}
peter = {'name': 'Peter', 'weeklyExercises': b,'weeklyTests': e} 
mike = {'name': 'Mike', 'weeklyExercises': c,'weeklyTests': f}
for _ in range(10):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))
    c.append(random.randint(0, 10))
    d.append(random.randint(0, 10))
    e.append(random.randint(0, 10))
    f.append(random.randint(0, 10))

students = [maria, peter, mike]

paso_a(maria)
avg_marks += maria['mark']
paso_a(peter)
avg_marks += peter['mark']
paso_a(mike)
avg_marks += mike['mark']


for i in range(len(students)):
    print(students[i]['name'])
    print(students[i]['weeklyExercises'])
    print(students[i]['weeklyTests'])
    print(students[i]['exam'])
    print(students[i]['mark'])
    print(students[i]['letterGrade'], end='\n\n')
 
print(avg_marks / len(students))