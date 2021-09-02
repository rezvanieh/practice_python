import re

print("Using Eval Function for Calculation")
print("Type 'quit' to exit\n")

previous = 0
run = True

def perform_math():
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("ٍEnter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print('Finished...')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '' , equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()
