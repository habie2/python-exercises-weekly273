"""
@title: excercise 9.
@author: Javier Sanz Diaz
@date: 2 Oct 2021

Create a program asking to enter the coordinates of a point in a plane, i.e. two integer
values, x and y, not equal to zero. The program must print the quadrant where this point lies (1
st quadrant if
x>0 and y>0, 2
nd
if x<0 and y>0, etc.) (Note: you can use the flow diagram of practice 2). For example for (1,1)
it must print: 1st. If x or y are zero it must print "The values are not valid" and finish
"""
 
x = int(input('Enter the x coordinate: '))
y = int(input('Enter the y coordinate: '))

if x == 0 or y == 0:
    print('The values are not valid.')
elif x > 0 and y > 0:
    print('1st')
elif x < 0 and y > 0:
    print('2nd')
elif x < 0 and y < 0:
    print('3rd')
else:
    print('4th')