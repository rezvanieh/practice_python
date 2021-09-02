def add(x , y):
    return x + y

def multiply(x , y):
    return x * y

def divide(x , y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = "Error..."
        print("Oops!  division by zero.  Try again...")
    return result

def subtract(x , y):
    return x - y



print("Choice operation(Zero to Exit): ")
print(""" 1. Add
              2. Multiply
              3. Divide
              4. Subtract
              0. Exit
        """)
 
while True:   
    try :
        op = int(input("Operation: "))
    
        if op == 0:
            break
        elif op in range(1,5):
            num1 = int(input("Number1: "))
            num2 = int(input("Number2: "))

            if op == 1 :
                print("{} + {} = {}".format(num1 , num2 , add(num1 , num2)))
            elif op == 2:
                print("{} * {} = {}".format(num1 , num2 , multiply(num1 , num2)))
            elif op == 3:
                result =  divide(num1 , num2)
                print("{} / {} = {}".format(num1 , num2 ,result))
            elif op == 4:
                print("{} - {} = {}".format(num1 , num2 , subtract(num1 , num2)))
        else :
            print("Oops!  That was no valid number.  Try again...")

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    
             
            
