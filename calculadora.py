import math


class Calculator(object): #Class calculator 
    def __init__(self): #Stores all attributes of class
        pass 

    def sum(self,a,b): 
        #method sum
        # Receives:
        # (a:int or float, b:int or float)
        # Returns:
        # a+b:int or float

        return a+b
    
    def sub(self,a,b):
        # Method sub
        # Receives:
        # (a:int or float, b:int or float)
        # Returns:
        # a-b:int or float
        return a-b

    def mult(self,a,b):
        # Method sub
        # Receives:
        # (a:int or float, b:int or float)
        # Returns:
        # a-b:int or float
        return a*b

    def div(self,a,b):
        # Method sub
        # Receives:
        # (a:int or float, b:int or float)
        # Returns:
        # a-b:int or float
        return a/b
    
    def mod(a,b):
        # Method mod
        # Receives:
        # (a:int, b:int)
        # Returns:
        # The remainder of the division from a/b

        a = int(a)
        b = int(b)

        return a%b
    
    def power(a,b):
        # Method power
        # Receives:
        # (a:int or float, b:int or float)
        # Returns:
        # a**b:int or float
        return a**b
    
    def root(a,b):
        # Method power
        # Receives:
        # (a:int or float, b:int or float)
        # Returns:
        # the bth root of a: int or float
        return a**(1/b)