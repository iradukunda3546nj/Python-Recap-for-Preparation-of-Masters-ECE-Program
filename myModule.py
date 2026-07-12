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
    raise TypeError("the value of x is not integer type") 
def my_name():
    print("clever")

---------------------------------------------------------------------------------------------------'''
import datetime
class BankAccount:

    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin                  # Private
        self.__balance = 0                # Private
        self.__daily_limit = 500000       # Private
        self.__withdrawn_today = 0        # Private
        self.__transactions = []          # Private

    # --------------------------
    # Private Methods
    # --------------------------
    def __changePin(self, oldPin):
      attempts = 0

      while attempts < 3:
        if oldPin == self.__pin:
            self.__pin = int(input("Enter the new PIN: "))
            print("New PIN has been set successfully!")
            return

        attempts += 1

        if attempts == 3:
            print("Account locked! Too many incorrect attempts.")
            return

        print(f"Incorrect PIN. {3 - attempts} attempt(s) remaining.")
        oldPin = int(input("Enter your current PIN again: "))
    
    def __verify_pin(self, entered_pin):
        return entered_pin == self.__pin

    def __account_active(self):
        # Imagine checking the bank database
        return True

    def __fraud_check(self, amount):
        # Simple fraud rule
        if amount > 300000:
            print("Fraud monitoring: Large transaction detected.")

    def __record_transaction(self, transaction):
        self.__transactions.append(transaction)

    # --------------------------
    # Public Methods
    # --------------------------
    def pinChange(self):
        ans=str(input("Do you truly want to change PIN  yes/no? :")).lower()
        if ans=="yes":
            oldPin=int(input("enter the old pin:"))
            self.__changePin(oldPin)
        else:
            print("Pin change cancelled")

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        self.__record_transaction(f"at {datetime.datetime.now()},Deposited {amount} ")

        print(f"{amount} RWF deposited successfully.")

    def withdraw(self, amount, pin):

        if not self.__account_active():
            print("Account is inactive.")
            return

        if not self.__verify_pin(pin):
            print("Incorrect PIN.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        if self.__withdrawn_today + amount > self.__daily_limit:
            print("Daily withdrawal limit exceeded.")
            return

        self.__fraud_check(amount)

        self.__balance -= amount
        self.__withdrawn_today += amount

        self.__record_transaction(f"at {datetime.datetime.now()},Withdrew {amount}")

        print(f"{amount} RWF withdrawn successfully.")

    def show_balance(self):

        print(f"Current Balance: {self.__balance} RWF")

    def show_transactions(self):

        print("\nTransaction History")

        for transaction in self.__transactions:
            print("-", transaction)


#Using the class
account = BankAccount("Jean Claude", 1234)

account.deposit(100000)

account.deposit(250000)

account.show_balance()

print()

account.withdraw(50000, 1111)

print()

account.withdraw(500000, 1234)

print()

account.withdraw(100000, 1234)

print()

account.show_balance()

print()

account.show_transactions()
account.pinChange()
