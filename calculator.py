def operation(num1 , num2 , op):
    result = 0
    if op == 1:
        result = num1 + num2
        print("{} + {} = {}".format(num1 , num2, result))
    elif op == 2:
        result = num1 * num2
        print("{} * {} = {}".format(num1 , num2, result))
    elif op == 3:
        try :        
           result = num1 / num2
           print("{} / {} = {}".format(num1 , num2, result))
        except ZeroDivisionError:
            print("Oops!  division by zero.  Try again...")                                    
        
    elif op == 4 :
        result = num2 - num1
        print("{} - {} = {}".format(num2 , num1, result))

    return result

print("Please choice operation form list below( zero to Exit)")
op = 1
while True:
    print(""" 1. Add
            2. Multiplication
            3. Divition
            4. Sub
            0. Exit
        """)
    try :
        op = int(input("Operation: "))
    
        if op == 0:
            break
        elif op in range(1,5):
            num1 = int(input("Number1: "))
            num2 = int(input("Number2: "))
            operation(num1 , num2 , op)
        else :
            print("Oops!  That was no valid number.  Try again..")
            
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    
             
            
