n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
op = input('Input the operator(+,-, *, /) : ')

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print("invalid input! ")


