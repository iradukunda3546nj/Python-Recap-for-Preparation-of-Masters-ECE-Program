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

#escape characters :are used to insert characters that are illegal in a string, for example, if you want to insert a double quote in a string that is defined by double quotes, you can use the escape character \ to escape the double quote.
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
-----------------------------------------------------"""

#Now, we are going to see how to use sets in python, sets are used to store multiple items in a single variable, they are unordered, unchangeable, and do not allow duplicate values. Sets are written with curly brackets {}.
mySet={"laptop","phone","TV","laptop"} #this set has duplicate values, but it will only store unique values.
print(mySet)#this will print the set with unique values only, thus it will print {'TV', 'laptop', 'phone'} because the duplicate value "laptop" is removed.