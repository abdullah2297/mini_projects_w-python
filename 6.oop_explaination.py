## OOP Concepts:- 
# 1. Encapsulation
    # what happen in vegas still in vegas [Black Box]
    # Act like a black box which take inputs and return outputs but the user don't know what happen
    # Setters to edit and getters methods to look
    # Dealing with data through setters and getter
    # Add __ before the attribute

# 2. Polymorphism
# 3. Abstraction
# 4. Inheritance

# Class ==> is Container for all Instances, Start with Capital letter, 
# Class variables ==> All instances inherit the constructor variables, 
# init Function ==> is container for all Data, all instances can access this data, every time you create a new class will call this function
# Class Methods ==> 
# class method that can be called using ClassName.MethodName(). The class method can also be called using an object of the class 
# @classmethods, control class attr, take cls as param
# Instance ==> is called object and inherit all class Variables and methods
# Instance Methods ==> we can use it for all instances, assign self to every method
# Static Methods ==> 

from datetime import date
class Prospect:

    ## Class attr
    numOfProspects = 0 
    department = 'B2B'

    ## Initialization Function
    def __init__(self, name, company, title, p_num, funnel, closing = 'pending', age=None, prog = 0):
        self.name = name
        self.company = company
        self.title = title
        self.p_num = p_num
        self.closing = closing
        self.funnel= funnel
        self.age = age
        self.__prog = prog ## __ For Encapsulation purpose
        Prospect.numOfProspects +=1

    @classmethod
    def owner(cls):
        return cls('abdullah', 'Amit','b2b','01022',['contract'])
    ## class method
    ## Change department
    @classmethod   ## Any change happen will efect all instances
    def change_department(self,new_department):
        self.department = new_department
    ## Define set and get for ENCAPSULATION Purpose
    def setProg(self):
        if self.funnel[-1] != 'contract':
            if self.funnel[-1] == 'meeting':
                self.__prog = 3
            elif self.funnel[-1] =='Call':
                self.__prog = 1
        if self.funnel[-1] == 'contract':
            self.__prog = 5


    def getProg(self):
        return self.__prog

    ## instance Method
    def send_mail(self):
        msg = f"Hello {self.name}, as we know that you are {self.title} at {self.company} we wanna your {self.p_num} Thanks From {self.department} "
        return msg

    ## Instance Method
    def deal_status(self):
        if self.closing == 'won':
            print(f"deal is done '{self.closing}'")
        else:
            print(f"deal is still in progress'{self.closing}'")
    
    ## Instance Method
    def age_seg(self, seg):
        if self.age >=seg:
            print(f"Segmant is OLD")
        else:
            print(f"segmant is NEW")
            print(self.send_mail()) ## Recursive Function



## First Object from The Class
ahmed = Prospect('ahmed','Voda','Sales Manager', '010025',['Call','meeting','contract'],'won',25)

## Second Object from The Class
ali = Prospect('ali','Voda','Sales Manager', '010025',['Call','meeting'],age=40)

medo = Prospect('ali','Voda','Sales Manager', '010025',['Call'],age=40)

## Change some values
## This method againest Encapsulation Concept ## Check setProg Function
ali.company = "Etisalat"
ali.title = "Business developer"


## Test


