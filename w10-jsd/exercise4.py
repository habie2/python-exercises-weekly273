"""
@title: exercise4
@author: habi2
@date: 12/11/2021

Define a function that returns a tuple simulating the behaviour of the function
range(start,stop,step), which returns a sequence of numbers between the given start
integer to the stop integer incremented by the given step integer. Configure the function with
optional parameters so it also works to simulate functions range(start, stop) and
range(stop). You must check that the types of the parameters are correct (int) and that
their range is also correct. If not an empty tuple will be returned.
"""

def range_fn(start = 0, stop = None, step = 1):
    # If only one parameter is introduced, the parameter, then start will be 0, 
    # and stop the parameter that is is introduced at start. 
    if stop == None:
            stop = start
            start = 0

    if (type(start) or type(stop) or type(step)) != int:
        return ()
    elif start > stop:
        return ()
    else:
        lista = []
        num = start
        while num < stop:
            lista.append(num)
            num += step
        return tuple(lista)

print(range_fn(1,100))