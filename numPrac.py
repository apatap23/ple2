import random

'''
Part 1: Roll your Own
'''
#Create a function that make two lists of one million elements by calling random.random in a list comp 


def list_maker():
    a , b = [random.sample(range(0, 1000000), 1000000), random.sample(range(0, 1000000), 1000000)]

    print (a)
    print (b) 


def list_maker2():
    a , b = [random.random() for _ in range(5)], [random.random() for _ in range(5)]
    print(a)
    print(b)

list_maker2()
