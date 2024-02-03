# Calculator

def calculation (a,b,operation):
    
    if operation == '+':
        c = a + b
        print(c)
    
    elif operation == '-':
        c = a - b
        print(c)   
    elif operation == '*':
        c = a * b
        print(c)
    elif operation == '/':
        c = a / b
        print(c)


calculation (10,5,'+')