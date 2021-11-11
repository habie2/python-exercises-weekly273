"""
@title: excercise 1.
@author: Javier Sanz Diaz
@date: 14 Oct 2021

Create a list of any type. Assign one of its elements to another one (e.g. a[5] = a[3]). Print
both elements. Next, add a line changing the value of the second element, and print both
elements again. Does the first one also change? Why? What happens if the value of the first one
is changed?
"""
a = [1, 2, 3, 89, 5, 6]

print(f'a[5] ={a[5]}, a[3]{a[3]}')
a[5] = a[3]
print(f'a[5] ={a[5]}, a[3]{a[3]}')

'''
Conclusion:
The first one does not change, becasue it is giving the value of the first one
to the second one and not in the other way. Îf we change the value of the first
one, the value of the second one also changes.
'''