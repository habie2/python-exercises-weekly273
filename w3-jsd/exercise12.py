"""
@title: exercise12. Printing with format.
@author: Javier Sanz Diaz
@date: 26/09/2021

Copy the following program:

Execute it and check that you get the following outcome:
Let’s talk about Johnny Depp.
He’s 178 centimeters tall.
He’s 65.400000 kilograms heavy.
Actually that’s not too heavy.
He’s got Brown eyes and Brown hair.
In class, we saw a different use of the print function; that is, print("Let’s talk about", name). Copy the same program, but rewrite the print functions using the format that we saw in class. Is there any difference in the outcome between the two ways?

"""
name = 'Johnny Depp'
age = 55
height = 1.78
weight = 65.4
eyes = 'brown'
hair = 'brown'

"""
print("Let’s talk about %s." %name)
print("He's %i years old" %age)
print("He’s %.2f meters tall." %height)
print("He’s %.0f kilograms heavy." %weight)
print("Actually that’s not too heavy.")
print("He has %s eyes and %s hair." % (eyes, hair))
"""
print("Let’s talk about", age)
print("He's", age, "years old")
print("He’s ", height, "meters tall.")
print("He’s ", weight, " kilograms heavy.")
print("Actually that’s not too heavy.")
print("He has", eyes, " eyes and ",hair ," hair.")

"""
Conclusion: 

No, there is no difference between the two outcomes, but if in the first case we don not put the indicators of decimals that we want, the result would have been different, because we would have obtained the same number followed by a certain number of zeros until it gets to 6 decimals.
"""