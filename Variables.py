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
-------------------------------------------------
#this function will help me to calculate the coverage of wavelength of a signal given that it freq

ct=3e8 #speed of light in m/s
def wavCal(c):
    global freq
    freq=int(input("Enter the frequency of the signal in GHz: "))
    wavelength = c / (freq * 1e9)  # Convert GHz to Hz and calculate wavelength
    return wavelength
cal=wavCal(ct)
print("The wavelength of the signal is:", cal, "meters")
------------------------------------------------

#using random module to generate random numbers, python does not have a random() function but it has a random module which has a random() function that can be used to generate random numbers.
import random as rd
print(rd.randrange(1,10))
-------------------------------------------------

#Learning strings
print('here is "Jimy"')#tip: if you've used double quotes to define a string, you can use single quotes inside the string and vice versa."""
'''
a="""we are learning python programming to enhance our skills in writing robust and efficient 
computer program for different applications and to solve real world problems"""
print(a[1:100])
print(len(a))
for x in a:
    print(x)
print("python" in a) #checking if the word is in the string or not, it will return True or False
------------------------------------------------ 

x=("I'm going to take a lunch by 1PM today")

if "lunch" not in x:
    print("Yes, 'lunch' is present in the string")
else:
    print("No, 'lunch' is not present in the string") 
    ----------------------

x=("I'm going to take a lunch by 1PM today")
print(x[10:]) #this is known as slicing, it will print the string from the 10th index to the end of the string

------------------------------------- 
#String modification
a="Hello, Horld!"
print(a.upper())
print(a.strip()) #removes any whitespace from the beginning or the end
print(a.replace("H","j"))

if "h" not  in a:
    print("It's true that the letter h was replaced with j")
else:
    print("It's false that the letter h was replaced with j")

-----------------------------------------------------------------
#string modification cont'd

tx="How are you clever ?"
xrep=tx.replace("clever","good at Maths")
print(xrep)

-------------------------------------------------------

#split()
td="hello, jays"
print(td.split(',')) #This returns a list containing the words in the string, using ',' as the separator

-------------------------------------------------------

#concatenation of strings
a="Hello"
b=" my engineer Jean !"
print(a+b+",are you ready to learn python programming ?") #this is known as concatenation of strings, it will join the two strings together and print them as one string
--------------------------------------------------------'''

