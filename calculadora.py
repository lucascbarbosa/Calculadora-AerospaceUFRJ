class Calculator(object): #Class calculator 
    def __init__(self): #Stores all attributes of class
        pass 

    def add(self,a,b): 
        #method sum
        # Receives:
        # (a:int, b:int)
        # Returns:
        # a+b:int

        return a+b
    
    def sub(self,a,b):
        # Method add
        # Receives:
        # (a:int, b:int)
        # Returns:
        # a-b:int
        return a-b

    def mult(self,a,b):
        # Method sub
        # Receives:
        # (a:int, b:int)
        # Returns:
        # a-b:int
        return a*b

    def div(self,a,b):
        # Method sub
        # Receives:
        # (a:int, b:int)
        # Returns:
        # a-b:int
        return a/b
    
    def mod(self,a,b):
        # Method mod
        # Receives:
        # (a:int, b:int)
        # Returns:
        # The remainder of the division from a/b

        a = int(a)
        b = int(b)

        return a%b
    
    def power(self,a,b):
        # Method power
        # Receives:
        # (a:int, b:int)
        # Returns:
        # a**b:int
        return a**b
    
    def root(self,a,b):
        # Method power
        # Receives:
        # (a:int, b:int)
        # Returns:
        # the bth root of a: float
        return a**(1/b)
    
    def fib(self,x):
        # Method fib
        # Receives:
        # x: int
        # Returns
        # the x-th fibonacci number
        if x == 0 or x == 1:
            return 1
        else:
            return self.fib(x-1)+self.fib(x-2)



if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Awesome Calculator! Here are the instructions:\nType [number1] [operator] [number2 (if not needed type -)]\n The lists of operators are:\n+: sum\n-: subtraction\n*: multiplication\n/:division\n%: remainder\n^:potentiation\n~: radication.\n!: the [number1]-th fibonacci number\n")
    will = True # Boolean variable to determine if the user wishes to continue using calculator
    while will:
        a,op,b = input("Please insert desired operation: ").split()
        a = int(a) #the numbers must be int
        try: #If [number2] is not null
            b = int(b)
            if op == "+":
                answer = calc.add(a,b)

            if op == "-":
                answer = calc.sub(a,b)
            
            if op == "*":
                answer = calc.mult(a,b)

            if op == "/":
                answer = calc.div(a,b)
            
            if op == "%":
                answer = calc.mod(a,b)
            
            if op == "^":
                answer = calc.power(a,b)
            
            if op == "~":
                answer = calc.root(a,b)
            
            print(f'The answer of {a} {op} {b} is {answer}')
        except:
            if op == "!":
                answer = calc.fib(a-1)
                print(f"The {a}-th fibonacci number is {answer}")

        cont = input('Wish to continue (s/n)? ').lower()

        if cont == "n":
            will = False