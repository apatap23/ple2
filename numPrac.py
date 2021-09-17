import random

'''
Part 1: Roll your Own
'''
#Create a function that make two lists of one million elements by calling random.random in a list comp 


def list_maker():
    #a = random.sample(range(0, 1000000), 1000000)
    c , d = [random.sample(range(0, 1000000), 1000000), random.sample(range(0, 1000000), 1000000)]

    print (c)
    print (d) 

list_maker()
