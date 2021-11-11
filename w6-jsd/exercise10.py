"""
@title: excercise 10.
@author: Javier Sanz Diaz
@date: 19 Oct 2021

To measure the time a program takes to execute we can use the time library and two variables.
In the first one we will store the time when our program starts executing (start =
time.time() in the first line of our program) and in the second one we will store the time
when it finishes (end = time.time() in the last line). Create a program that randomly fills
three different lists with 100,000 random values in the range 1 to 100:
a) For the first list use the append() method
b) For the second one use the += operator
c) For the third one use the + operator
Measure the time each one of these lists takes to fill. Is there any difference?

"""
import time, random
list = []

#Method a)
start_a = time.time()

for _ in range(100_000):
    list.append(random.randrange(1, 101))

end_a = time.time()

del(list)
list = []

#Method b)
start_b = time.time()

list_b = []
for _ in range(100_000):
    list_b += [random.randrange(1, 101)]
end_b = time.time()

del(list)
list = []

#Method c)
start_c = time.time()

list_c = []
for _ in range(100_000):
    list_c = list_c + [random.randrange(1, 101)]
end_c = time.time()

print(f'''Time table:
Method a):
Start: {start_a}
End: {end_a}
Total time: {end_a - start_a}

Method b):
Start: {start_b}
End: {end_b}
Total time: {end_b - start_b}

Method c):
Start: {start_c}
End: {end_c}
Total time: {end_c - start_c}''')

'''
Yes, there is difference in the time that it takes to fill the list.
'''