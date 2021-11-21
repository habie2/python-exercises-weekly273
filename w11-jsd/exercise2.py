"""
@title: exercise2
@author: habi2
@date: 11/11/2021

Create a new type named RightTriangle to represent a right triangle, with fields base
and height. Create an init method that receives both fields as parameters and checks if they
are bigger than 0 (if not they will be set to 1). Write a program that uses the keyboard to read
the base and the height and store them in a RightTriangle object. Next it should ask
the user whether the area or the perimeter of the triangle has to be calculated and print the
resulting value.
"""
from exercise2class import RightTriangle

print(RightTriangle(int(input('base: ')), int(input('height: ')), input('area or perimmeter? (a/p) ')))

