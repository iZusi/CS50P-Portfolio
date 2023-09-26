# get user input
expression = (input('Expression: '))

# split user input into three parts with a whitespace and store each in a variable
x, y, z = expression.split(' ')

if '+' in expression:
    n = float(x) + float(z)
    print(round(n,1))
elif '-' in expression:
    m = float(x) - float(z)
    print(round(m,1))
elif '/' in expression:
    if float(z) == 0:
        print('Math Error!')
    else:
        o = float(x) / float(z)
        print(round(o,1))
elif '*' in expression:
    p = float(x) * float(z)
    print(round(p,1))
