'''myCredentials={
"name":"Jean Clever",
"age":25,
"city":"New York"
} 
----------------------------------------
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 
-----------------------------------------------------
#another way to create a dictionary
person={}
person["Name:"]="Jean Clever"
person["age"]=46
person[10]="ten"
print(person)

------------------------------------------------------------

#converting a dictionary into tuple//Let me convert this dictionary into the tuple
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Carol", "age": 19}
]

students_tuple=[(item["name"],item["age"]) for item in students]
print(students_tuple) 

-----------------------------------------------------------------
#converting a tuple into a dictionary /self-exercise
studentsx = [
    ("Alice", 20),
    ("Bob", 22),
    ("Carol", 19)
] 

students_dict=[{"name":item[0],"age":item[1]} for item in studentsx]
print(students_dict)

Takeaway: when dealing with data collections, it's always a good idea to use List Comprehension and bad idea to use for loop with append()
------------------------------------------------
import json
a=open("./ece_stream.json","r") # this helps us to open a file with help of open() method
c=json.load(a) #converting a json object into a python object
data_samples=c["samples"] #this is a dictionary containing all the samples
data_tuple=[(item["t"],item["reading"]) for item in data_samples]
print(data_tuple)

--------------------------------------

#Try---Eception concepts
x="hello"
if type(x) is not int:
    raise TypeError("the value of x is not integer type") '''
def my_name():
    print("clever")