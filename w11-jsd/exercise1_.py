"""
@title: exercise1
@author: habi2
@date: 11/11/2021

Create the Student class, which represents a first year student. Its fields will be: name,
surname, programming mark, algebra mark, calculus mark, physics mark,
skills mark and humanities mark. Create an init method that receives values for all the
fields and checks that the values for the marks are in the right range (if not, a zero will be
assigned to the mark). Write a program that creates an object of this type, fills the fields asking
the user by keyboard and prints them.
"""
from ClassExercise1 import Student

var1 = Student(input)