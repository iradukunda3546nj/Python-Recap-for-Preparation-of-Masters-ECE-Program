"""A.1. Task/Objective: Writing a function add_vectors(v1, v2) that returns the element-wise sum of two 2D vectors.
 # e.g. add_vectors([1, 2], [3, 4]) -> [4, 6]"""

def add_vectors(v1,v2):
    sumList=[]
    sumList.append(v1[0]+v2[0])
    sumList.append(v1[1]+v2[1])
    return sumList

v1=[1,2] #i.e. this is a 2D vector
v2=[3,4]
print(add_vectors(v1,v2))

"""A. 2. Write a function scale_vector(scalar, v) that multiplies every element of v by a scalar.
 # e.g. scale_vectors(3, [2, 1]) -> [6, 3] """
def scale_vector(scalar, v):
    scaledVector=[]
    scaledVector.append(scalar*v[0])
    scaledVector.append(scalar*v[1])
    return scaledVector

s=int(input("Enter the scaler:"))
v=[2,3]
print(f"The result of scaling vector {v} by {s} is {scale_vector(s,v)}")

"""A.3. Writing a function dot_product(v1, v2) that computes the dot product without using 
the built-in sum() function. Using a loop instead."""

def dot_product(v1,v2):
    result=[]
    for i in range(len(v1)):
        result.append(v1[i]*v2[i])
    return result

v1=[1,2]
v2=[3,4]
print(f"the product of two vectors {v1} and {v2} is {dot_product(v1,v2)}")


