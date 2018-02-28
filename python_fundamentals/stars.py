
from __future__ import print_function

#x = [4, 6, 1, 3, 5, 7, 25]

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arr):
    """this function prints stars accoirding to 
    the value of every index on a list and the 
    first letter in case the value is a string"""
    for i in arr:
        print ('\n')
        T = type(i)
        if T == int:
            for j in range(1, i+1):
                print ('*', end='')
        elif T == str:
            k = len(i)
            word = i[0]
            for l in range(1, k+1):
                print (word.lower(), end='')
    print ('\n')
draw_stars(x)
