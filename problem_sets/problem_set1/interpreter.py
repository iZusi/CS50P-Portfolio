# Get user input for a mathematical expression
expression = (input('Expression: '))

# Split the user input into three parts (x, operator, and z) using whitespace as the delimiter
x, y, z = expression.split(' ')

# Check the operator in the expression
if '+' in expression:
    # If '+' is found, perform addition and print the result rounded to one decimal place
    n = float(x) + float(z)
    print(round(n, 1))
elif '-' in expression:
    # If '-' is found, perform subtraction and print the result rounded to one decimal place
    m = float(x) - float(z)
    print(round(m, 1))
elif '/' in expression:
    # If '/' is found, check if dividing by zero and handle the error, or perform division and print the result rounded to one decimal place
    if float(z) == 0:
        print('Math Error!')
    else:
        o = float(x) / float(z)
        print(round(o, 1))
elif '*' in expression:
    # If '*' is found, perform multiplication and print the result rounded to one decimal place
    p = float(x) * float(z)
    print(round(p, 1))
