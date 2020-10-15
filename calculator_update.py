print('Welcome to the calculator!')
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
opr = input('Enter Operator : ')
if opr == "+":
  print(f"The sum is {a + b}")
elif opr == "-":
  print(f"The sum is {a - b}")
elif opr == "*":
  print(f"The sum is {a * b}")
elif opr == "/":
  print(f"The sum is {a / b}") 
else: 
  print('Unable to identify') 
