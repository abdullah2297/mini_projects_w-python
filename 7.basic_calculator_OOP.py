
## Basic Claculator
import numpy as np
class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b



while True:
    
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    ch = int(input("Select operation: "))
    
    #Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 5):
        
        #first check whether user want to exit
        if(ch == 5):
            break
        
        #If not then ask fo the input and call appropiate methods        
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        my_cl = Calculator(a,b)

        if(ch == 1):
            print(f"{a} + {b} = {my_cl.add()}")
        elif(ch == 2):
            print(f"{a} - {b} = {my_cl.subtract()}")
        elif(ch == 3):
            print(f"{a} * {b} = {my_cl.multiply()}")
        elif(ch == 4):
            print(f"{a} / {b} = {my_cl.divide()}")

    else:
        print("Invalid Input")




