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
--------------------------------------------------------

#Formatting strings  //we use format() method to format strings in python
age=36
name="John"
print(f"My name is {name} and I am {age} years old. how about you?") #this is known as f-string formatting, it will replace the variables with their values and print them as one string

#placeholder and modifiers
age=26
calweight=70.789
print(f" I am {age} years old and my weight is {calweight:.2f} kg") #this is known as f-string formatting, it will replace the variables with their values and print them as one string, the modifier .2f will round the value of calweight to 2 decimal places

-----------------------------------------------------------------------------------

#escape characters :are used to insert characters that are illegal in a string, for example, if you want to insert a double quote in a string that is defined by double quotes, you can use the escape character \\ to escape the double quote.
y="we are learning \"python\" programming to enhance our programming skills."
print(y) #this will print the string y with the double quotes around the word "python"
print(y.count("python")) #this will count the number of times the word "python" appears in the string y
print(y.find("python")) #this will return the index of the first occurrence of the word "python" in the string y
print(y.encode()) # this will encode the string y into bytes using the default encoding (utf-8)

--------------------------------------------------------------

#Boolean 
def myBool():
    x=10
    y=20
    if x>y:
        return True
    else:
        return False

if myBool():
    print("x is greater than y")
else:
    print("x is not greater than y")
    

#Ternary operator in python
x=3;
y="friday" if x==5 else "saturday" if x==6 else  "wednesday" if x==3 else "sunday"
print(y) 
--------------------------------------------------------------
#Testing bitwise operators in python
x=64
y=16
z=4
print(16<<2) #bits manupulation i.e shift by 2 bits to the left , same as multiplying by 2^2=4, so 16*4=64
print(64>>2) #bits manipulation i.e shift by 2 bits to the  right, same as dividing by 2^2  i.e (n>>x)=n/t where t=2^x


mylist=["Kamana","Kankwanzi","Rumanzi","Manzi"]
#print(mylist.count("Manzi"))
mylist[1]="Kweza"
mylist.append("Mwiza")
mylist.remove(mylist[1])
print(mylist)#observed that lists are ordered and mutable/i.e changeable i.e you can add,edit, remove a data

mytuple=("year","month","day")
print(mytuple) #obeserved that the tuples are ordered(indexing) however, they are not mutable i.e you can't change anything once created, it's kind of ROM, uses cases:  GPS location (lat,long),  time and date format (yy:mm:dd),etc, basically , use tuples for fixed data type.

#sets: sets are allows only unique elements i.e. it has no duplicate elements like a list, let's say we wantto build an application to tell us types of devices connected to the wi-fi, here we might have laptop,laptop,phone,TV,  so the set will show {laptop,phone,TV}
#sets are useful when you want to work on IDS, MAC IDS, students IDs,IP Addresses.


#adding and removing items in a list
myData=["coz","miz","tiz","poc","jaz"]
myData[1:3]=["mit","fake"]
myData.insert(2,"Clever")
myData.append("Turye")
myData.insert(1,"orange")
print(myData)

#extending/ all adding the elements of two Lists together
myPoints=["elec","magnetic","champ"]
myPoints.extend(myData)
print(myPoints)
#you can remove an element from the List using remove()
myPoints.remove("jaz")
print(myPoints)

#we can use pop() when we want to remove an element based on the index.
myPoints.pop(1)
myPoints.pop()#if you do not specify the index, it automatically removes the last item in the List
print(myPoints)
 #we can use del keyword to delete either the item at specified index or delete whole list.
del myPoints[1]#will delete item at index 1 in the myPoints list
#del myPoints #completely delete a list and it's different from clearing the list, this act delete even variable
myPoints.clear() #this one flushes the list but doesn't delete it
print(myPoints)

--------------------------------------------------------------------'''
#Looping through the List

mem=[24, 45, 67, 89, 70]
"""for i in mem:
    if i==67:
        print("I've got 67 in the list")
    else:
        print("")
print("done")
------------------------------------------------------------


#Alternatively, you can use while loop

i=0
while i<(len(mem)):
    if mem[i]==67:
        print("I 've got 67 in the list")
    else:
        print("")
    i+=1
---------------------------------------------------------------------------"""
#List comprehension: the way you can create a new list based on other list e.g you have fruits list and you want
#a new list of fruits cona with letter 'a' from the existing list

myFruits=["apple","melon","banana","passion","papaya","dmelon","peanaple"]
"""newList=[]

for i in myFruits:
    if "a" in i:
        newList.append(i)
print(newList)
#the above example was using for loop with conditional test inside, now, we need to use the List comprehension to show how it uses only one line to do that
newList=[x for x in myFruits if 'a' in x]  #this is a know as a list comprehension
print(newList) 
-------------------------------------------------------------------

#second example about selecting only even numbers from list of many numbers using List Comprehension
myDatx=[2,57,8,90,68,47,28,59,93]
newDatx=[x for x in myDatx if x%2==0]
print(newDatx)
--------------------------------------------------
#Sorting in the list using sort()
myPeople=["Akimana","Latifa","Keza","Amina","aior","Abdoul"]
#myPeople.sort()#sort based on alphebetical letters(with Capital letter being treated with higher priority).
myPeople.sort(key=str.lower)
print(myPeople)

mych=[3,1,2]
mych.sort(reverse=True)
print(mych)
-----------------------------------------------------
#copying the List using copy() or list() method.,
#you can just copy list by saying list2=list1 because, in this way, whatever changed from list1 will be eqaully changed in list2 as list2 reference to list1

myList=[2,8,5,7]
#newList=myList.copy()#using a copy method
newList=list(myList)#using a list()
newList=myList[:]#using : operator.
print(newList)

#Joing the two or more Lists, you can join the Lists using "+" , extend()
list1=[1,2,3,4,5,6,7,8,8,9,9]
list2=[9,8,7,6,5,4,3,2,1]
#newList=list1+list2 #joining list using '+' operator
newList=list1.extend(list2)
print(newList)
----------------------------------------------------

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])  #from exercises, this prints the "mango""

-------------------------------------------------------

[print(x) for x in ['apple', 'banana', 'cherry']] #other way of printing the list using list comprehension, this is known as a one liner code

---------------------------------------------------------

#Tuples: Tuples are used to store multiple items in a single variable, they are ordered and unchangeable (immutable), and allow duplicate values. Tuples are written with round brackets ().
myTuple=("apple","banana","cherry")
print(myTuple)
#if the tuple has only one item, you have to add a comma after the item, otherwise it will not be recognized as a tuple.
myTuple1=("apple",)
print(myTuple1)
#checking if the element exists in the tuple
if "apple" in myTuple:
    print("Yes, 'apple' is in the tuple")
#updating tuples: you cannot change the values of a tuple, but you can convert it to a list, change the values, and convert it back to a tuple.
myTuple2=("apple","banana","cherry")
tupUpdate=list(myTuple2)
tupUpdate[1] = "kiwi"
myTuple2=tuple(tupUpdate)
print(myTuple2)#tuple is now updated with the new value "kiwi" instead of "banana"
#you can also add or remove items from a tuple by converting it to a list, adding or removing the items, and converting it back to a tuple.
#you can also add items to a tuple by concatenating two tuples together.
myTuple3=("apple","banana","cherry")
myTuple4=("date","elderberry")
myTuple3=myTuple3+myTuple4
print(myTuple3)#this will print the new tuple with the added items from myTuple4

#Unapacking a tuple: when we create a tuple, we normally assign values to it. This is called "packing" a tuple. But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".
myTuple5=("apple","banana","cherry")
#unpacking the tuple into variables
(x,y,z)=myTuple5
print(x)#this will print "apple"    
print(y)#this will print "banana"
print(z)#this will print "cherry"
#the number of varibles must match the number of values in the tuple, otherwise,python will assign remaining values to the last variable as a list.thus remember to use asterisk * to assign the remaining values to the last variable as a list.
myTuple6=("apple","banana","cherry","date","elderberry")
(x,y,*z)=myTuple6
print(x)#this will print "apple"    
print(y)#this will print "banana"
print(z)#this will print the remaining values as a list ["cherry","date","elderberry"]

#Looping through a tuple: you can loop through the tuple items by using a for loop.
myTuple7=("apple","banana","cherry")
for i in myTuple7:
    print(i)#this will print each item in the tuple on a new line 
#Looping using a range() function: you can also loop through the tuple items by using a for loop and the range() function.  
myFruits=("apple","banana","cherry")
for i in range(len(myFruits)):
    print(myFruits[i])#this will print each item in the tuple on a new line using the index of the items
-----------------------------------------------------

#Now, we are going to see how to use sets in python, sets are used to store multiple items in a single variable, they are unordered, unchangeable, and do not allow duplicate values. Sets are written with curly brackets {}.
mySet={"laptop","phone","TV","laptop"} #this set has duplicate values, but it will only store unique values.
print(mySet)#this will print the set with unique values only, thus it will print {'TV', 'laptop', 'phone'} because the duplicate value "laptop" is removed.
#onc the set is created, you cannot change its items, but you can add new items to the set using the add() method.
mySet.add("tablet")#this will add the new item "tablet" to the set
print(mySet)#this will print the updated set with the new item "tablet"
#To add items from another set into the current set, you can use the update() method.
mySet1={"laptop","phone","TVx"}
mySet.update(mySet1)#this will add the items from mySet1 to mySet
print(mySet)#this will print the updated set with the new items from mySet1
#with update() method, you can add any iterable object (list, tuple, dictionary) to the set.
mySet2=["camera","printer"]
mySet.update(mySet2)#this will add the items from mySet2 to mySet
print(mySet)#this will print the updated set with the new items from mySet2

#for removing items from a set, you can use the remove() or discard() method. The difference between the two is that remove() will raise an error if the item does not exist, while discard() will not raise an error.
mySet.remove("phone")#this will remove the item "phone" from the set
mySet.discard("TV")#this will remove the item "TV" from the set
print(mySet)#this will print the updated set with the item "phone" removed
#you can also use the pop() method to remove a random item from the set, since sets are unordered.
mySet.pop()#this will remove a random item from the set

#Looping through a set: you can loop through the set items by using a for loop.
mySet3={"laptop","phone","TV"}
for i in mySet3:
    print(i)#this will print each item in the set on a new line
#for in range(len(mySet3)):
    #print(mySet3[i])#this will raise an error because sets do not support indexing, thus you cannot access items in a set by index.
#joining two sets: you can join two sets by using union()/update(), intersection(), difference(), symmetric_difference() methods.
setA={"laptop","phone","TV"}
setB={"tablet","TV","printer"}
setC=setA.union(setB)#this will join the two sets and store the result in setC
print(setC)#this will print the joined set  
setD=setA.intersection(setB)#this will return the common items in both sets, 
print(setD)#this will print the common items in both sets
setE=setA.difference(setB)#this will return the items that are in setA but not in setB
print(setE)#this will print the items that are in setA but not in setB
#tips to join multiple sets: you can join multiple sets by using the union() method or the update() method.
setF={"laptop","phone","TV"}
setG=setA.union(setB,setF)#this will join the three sets and store the result in setG
print(setG)#this will print the joined set
#or we can use | operator to join multiple sets
setH=setA|setB|setF#this will join the three sets and store the result in setH
print(setH)#this will print the joined set  
---------------------------------------------------------
#Now, we are going to see how to use dictionaries in python, dictionaries are used to store data values in key:value pairs, they are unordered, changeable, and do not allow duplicate keys. Dictionaries are written with curly brackets {}.   
thisDict={
    
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisDict)#this will print the dictionary with the key:value pairs
print(thisDict["year"])#this will print the value of the key "year" in the dictionary
#using the get() method to access the value of a key in the dictionary
print(thisDict.get("model"))#this will print the value of the key "model"
print(thisDict.keys())#this will print all the keys in the dictionary
thisDict["color"]="red"#this will add a new key:value pair to the dictionary
print(thisDict)#this will print the updated dictionary with the new key:value pair
print(thisDict["color"])#this will print the value of the key "color"
thisDict["year"]=2020#this will change the value of the key "year" in the dictionary
print(thisDict)#this will print the updated dictionary with the changed value of the key "year"
thisDict["taxable"]=True#this will add a new key:value pair to the dictionary
print(thisDict)#this will print the updated dictionary with the new key:value pair

#removing items from a dictionary: you can remove items from a dictionary by using the pop() method, popitem() method, or the del keyword.
thisDict.pop("model")#this will remove the key:value pair with the key "model" from the dictionary
print(thisDict)#this will print the updated dictionary with the key:value pair removed
#we can also use del keyword to remove a key:value pair from the dictionary
del thisDict["taxable"]#this will remove the key:value pair with the key "taxable" from the dictionary
print(thisDict)#this will print the updated dictionary with the key:value pair removed

#pay attention when using del keyword to remove a key:value pair from the dictionary, if you use del thisDict, it will delete the entire dictionary and you will not be able to access it anymore.  
#del thisDict#this will delete the entire dictionary
#we can also use the clear() method to remove all items from the dictionary, but it will not delete the dictionary itself.
#thisDict.clear()#this will remove all items from the dictionary

#Looping through a dictionary: you can loop through the dictionary items by using a for loop.

for i,y in thisDict.items():
    print(i,y)#this will print all the keys and values in the dictionary

for i in thisDict.keys():
    print(i)#this will print all the keys in the dictionary

for i in thisDict.values():
    print(i)#this will print all the values in the dictionary
##copying a dictionary: you can copy a dictionary by using the copy() method or the dict() function.
newDict=thisDict.copy()#this will create a copy of the dictionary
print(newDict)#this will print the copied dictionary
#copying a dictionary using the dict() function
newDict1=dict(thisDict)#this will create a copy of the dictionary
print(newDict1)#this will print the copied dictionary
#Nested dictionaries: you can create a nested dictionary by using a dictionary inside another dictionary.
myFamily={
    "child1":{
        
        "name":"Emmanuel",
        "year":2004
    },
    "child2":{
        
        "name":"Amina",
        "year":2006
    }
}
print(myFamily)#this will print the nested dictionary
print(myFamily["child1"]["year"])

#trying my own example of nested dictionary, let's say we have a collection of nodes with their respective sensor data, we can create a nested dictionary to store this information.
nodesCol={
    "sensor1":{
        "name":"temperature","value":25.5
    },
    "sensor2":{
        "name":"humidity","value":60
    },
    "sensor3":{
        "name":"pressure","value":1013
    }
}
print(nodesCol["sensor1"]["value"])
----------------------------------------------------------
allowedToVote=True
print("You are allowed to vote" if allowedToVote else "You are not allowed to vote")
#Using logic operators in python, we can use the and, or, not operators to combine conditional statements.
hasID=True
isCitizen=True
age=20
if hasID and isCitizen and age>=18:
    print("You are allowed to vote")
else:
    print("You are not allowed to vote")

#using match statement in python, match statement is used to compare a value against a series of patterns and execute the corresponding block of code. It is similar to switch statement in other programming languages.
day=int(input("Enter a number between 1 and 7 to represent the day of the week: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input, please enter a number between 1 and 7")

#second example of match statement
name=str(input("Enter your name: "))
match name:
    case "Emmanuel":
        print("Hello Emmanuel, welcome to the python programming world")
    case "Amina":
        print("Hello Amina, welcome to the python programming world")
    case "Jean":
        print("Hello Jean, welcome to the python programming world")
    case _:
        print("Hello stranger, welcome to the python programming world")
---------------------------------------------------------------------------
#Understanding the range() function
#range(n) function generates a sequence of numbers from 0 to n-1, it is commonly used in for loops to iterate over a sequence of numbers.
#range(start, stop, step) function generates a sequence of numbers from start to stop-1, with a step value of step. The default value of start is 0 and the default value of step is 1.
for i in range(2,20,2):#this will print the even numbers from 2 to 18
    print(i) #it prints 2,4.....................,18
------------------------------------------------------------------------

#Lambda function: a lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is commonly used as a shortcut for defining simple functions.
x=lambda a,c: a+c
print(x(5,10))#this will print 15
--------------------------------------------------------------
import myModule as nm   #learning how to import a module in python, we can use the import statement to import a module and use its functions and variables in our code. We can also use the as keyword to give the module a different name, which is useful when the module name is long or when we want to avoid naming conflicts with other modules.
import platform
x=nm.myCredentials["name"]
y=nm.myCredentials["age"]
print(f"My name is {x} and I am {y} years old.")
print(f"My operating system is {platform.system()} and its version is {platform.version()}.")
x=dir(platform)#this will print all the attributes and methods of the platform module
print(x)
--------------------------------------------------------
#importing from module, we can use the from keyword to import specific functions or variables from a module, instead of importing the entire module. This is useful when we only need to use a few functions or variables from a module, and it can also help to reduce memory usage and improve performance.
from myModule import greeting
greeting("Jean Clever") #this will print "Hello, Jean Clever"

from myModule import person1
print(f"My name is {person1['name']}, I am {person1['age']} years old, and I live in {person1['country']}.")

---------------------------------------------------------------
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) #this will print the day of the week

-------------------------------------------------------------------

#Bu using the math built-in module, we can perform mathematical operations in python. The math module provides a wide range of mathematical functions and constants, such as trigonometric functions, logarithmic functions, and constants like pi and e. We can use the import statement to import the math module and use its functions in our code.
import math
#we can use functions such as ceil,floor,pow,abs,sqrt,factorial,log,log10,log2,sin,cos,tan,asin,acos,atan,degrees,radians,pi,e
x=math.ceil(4.7)#this will round the number 4.7 up to the nearest integer, which is 5
y=math.floor(4.7)#this will round the number 4.7 down to the nearest integer, which is 4
z=math.pow(2,3)#this will calculate 2 raised to the power of 3, which is 8.0
a=math.sqrt(16)#this will calculate the square root of 16, which is 4.0
b=math.factorial(5)#this will calculate the factorial of 5, which is 120
c=math.log(100,10)#this will calculate the logarithm of 100 to the base 10, which is 2.0
d=math.log10(1000)#this will calculate the logarithm of 1000 to the base 10, which is 3.0
e=math.log2(8)#this will calculate the logarithm of 8 to the  base 2, which is 3.0
f=math.sin(math.radians(30))#this will calculate the sine of 30 degrees, which is 0.5
g=math.cos(math.radians(60))#this will calculate the cosine of 60   degrees, which is 0.5
h=math.tan(math.radians(45))#this will calculate the tangent of 45 degrees, which is 1.0
i=math.asin(0.5)#this will calculate the arcsine of 0.5, which is 30.0 degrees
j=math.acos(0.5)#this will calculate the arccosine of   0.5, which is 60.0 degrees
k=math.atan(1)#this will calculate the arctangent of 1, which   is 45.0 degrees
--------------------------------------------------------------------------------
#JSON: JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. In Python, we can use the built-in json module to work with JSON data. We can use the json.dumps() method to convert a Python object into a JSON string, and the json.loads() method to convert a JSON string into a Python object.

#I have realized that we can convert a plain text into a json equivalent and keep in mind that we use key-pairs style just as for dictionary, and note that all keys and strings must be enclosed in double quotes, and the values can be of any data type, including numbers, strings, lists, and other JSON objects.
#e.f

a='''"John Doe is a 28-year-old software engineer living in New York. He is currently employed 
full-time and has two primary skills: Python and JavaScript.'''
 
b={
  "name": "John Doe",
  "age": 28,
  "occupation": "Software Engineer",
  "location": "New York",
  "isFullTime": true,
  "skills": [
    "Python",
    "JavaScript"
  ]
}

#Observation: b is a json equivalent of a, and we can use the json.dumps() method to convert b into a json string, and the json.loads() method to convert a json string into a python object.

---------------------------------------------------------------------------
#we can convert a json into a python (resulting into a dictionary) using the json.loads() method, and we can convert a python object into a json string using the json.dumps() method.
import json
b={
  "name": "John Doe",
  "age": 28,
  "occupation": "Software Engineer",
  "location": "New York",
  "isFullTime": True,
  "skills": [
    "Python",
    "JavaScript"
  ]
}
json_string = json.dumps(b)  # convert the dict into a JSON string
x = json.loads(json_string)  # convert the JSON string back into a Python dict
print(x["skills"])  # this will print the python object (dictionary)
print(json_string)  # this will print the JSON string
-------------------------------------------------------------------
#Using Try,except,finally statements in python //simply saying: teh except section is executed when try section raises an error, and the finally section is executed regardless of whether an error occurred or not.
x=0
try:
    y=10/x
    print(y)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block is always executed.")
---------------------------------------------------------------------------------
#Use of raise statement in python, we can use the raise statement to raise an exception when a certain condition is met. This is useful when we want to enforce certain rules or constraints in our code.
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    else:
        print("Age is valid.") 

check_age(2)  # this will print ValueError: Age must be at least 18.

---------------------------------------------------------------------------------------
#File handling in python, we can use the open() function to open a file and perform various operations on it, such as reading, writing, and appending. We can also use the with statement to automatically close the file after we are done with it.
f=open(r"C:\Users\CMU_Loaner 207\Downloads\test.txt","a")  # open a file in append mode
f.write("\nNow the file has been updated.")  # write to the file
x=open(r"C:\Users\CMU_Loaner 207\Downloads\test.txt","r")  # open the file in read mode
print(x.read())  # read the contents of the file

#the open() function takes two arguments: the file path and the mode. The mode can be "r" for read, "w" for write, "a" for append, and "x" for exclusive creation. We can also use "b" for binary mode and "+" for read and write mode.

-------------------------------------------------------------------
#we can also delete a file using the os module, we can use the os.remove() method to delete a file. We can also use the os.rmdir() method to delete an empty directory, and the shutil.rmtree() method to delete a directory and all its contents.
import os   
os.remove(r"C:\Users\CMU_Loaner 207\Downloads\test.txt")  # delete the file
----------------------------------------------------------"""
d = {"a": 1, "b": 2} #example from canvas quiz
x= d.get("c", 0)
print(x)#this will print 0 because the key "c" does not exist in the dictionary, and we have provided a default value of 0 to return when the key is not found.
