# CS121 Lab 3: Functions

import math

# Your distance function goes here 

def dist(a, b):
    '''
    Input two vertices a, b which represent points with coordinates 
    a = [x1, y1] and b = [x2, y2] respectively.
    The function will compute the distance between the two points. 

    Input: vertices a, b where a = [x1, y1], b = [x2, y2] where contents of vertices are floats.
    Output: distance between two points. 
    '''
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return distance


# Your perimeter function goes here 

def peri(a, b, c):
    '''
    Input three vertices a, b, c which represent points with 
    coordinates (x1, y1), (x2, y2), and (x3, y3) respectively.
    The function will compute sum of the distance between the three points.
    '''
    perimeter = dist(a, b) + dist(a, c) + dist(b, c)
    return perimeter

def go():

    '''
    Write a small amount of code to verify that your functions work

    Verify that the distance between the points (0, 1) and (1, 0) is
    close to math.sqrt(2)

    After that is done, verify that the triangle with vertices at 
    (0, 0), (0, 1), (1, 0) has a perimeter 2 + math.sqrt(2)
    '''

    # replace the pass with code that calls your functions
    # and prints the results
    pass

if __name__ == "__main__":
    go()
    
                

