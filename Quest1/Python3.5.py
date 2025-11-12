from Python3 import multiply
from Python3 import divide
from Python3 import add
from Python3 import subtract
from Python3 import quotient
from Python3 import calculate

num1 = int(input("Enter a number: " ))
num2 = int(input("Enter a second number: "))
operation = input("Enter an operation: ")
result = calculate(num1, num2, operation)

print("result: " + str(result))