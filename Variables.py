"""import sys
print (sys.version)
print("hello world !", sep="")
print("Have a good day !", end="")
print ("Learning python is fun")

print ("I am", 25,"years old")
x=(" That was my name so far !")
x=(4)
print(x)

---------------------------------------------------------------------

y=type("John")
print(y)

_8man=6 #the variable name can start with an underscore and a number but not with a number only
print(_8man+6)

#different cases for varible naming
myVariableName = "John" #camelCase when only first letter of the variable name is in lower case and the first letter of the next word is in upper case
MyVariableName = "John" #PascalCase when the first letter of the variable name and the first letter of the next word is in upper case
my_variable_name = "John" #snake_case when the variable name is in lower case and the words are separated by an underscore
-------------------------------------------------------------------------------------

#assigning mutiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x,end="",)
print(y)
print(z)

------------------------------------------------------------  

#we can also assign the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

------------------------------------------------

#Unpacking a collection
fruits=["Apple","Banana","Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
-----------------------------------------------
x="Python"
y="is"
z="awesome !"
#print(x+y+z) #Pythonisawesome !
print(x,y,z) #Python is awesome !
--------------------------------------------

#Global variables can be used anywhere in the program and can be accessed inside a function by using the global keyword.
x=int(input("Enter a number: "))
def myfunc(x):
     
     z=10+x #you see now that the variable x is being used inside the function myfunc() and it is a global variable because it is defined outside the function.
     print("The sum of ten and the entered number is",z)

myfunc(x)

------------------------------------------------
#x= "Python is great"
def myPrint():
    global x
    x="Python is fun"
    
myPrint()
print(x) # when you want to use a variable from function (i.e it's local variable) outside the function you have to declare it as global variable inside the function.
-------------------------------------------------"""


