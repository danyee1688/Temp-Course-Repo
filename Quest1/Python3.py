def say_hello():
    print("Hello World")

say_hello()

print("---------------------------")

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def quotient(x, y):
    return x % y

def calculate(x: int, y: int, function_name: str):
    if function_name == "add":
        return add(x, y)
    elif function_name == "subtract":
        return subtract(x, y)
    elif function_name == "multiply":
        return multiply(x, y)
    elif function_name == "divide":
        return divide(x, y)
    elif function_name == "quotient":
        return quotient(x, y)
    else:
        return "function name not found"

print("1 + 2 = " + str(calculate(1, 2, "add")))
print("2 - (-1) = " + str(calculate(2, -1, "subtract")))
print("2000 * 1.5 = " + str(calculate(2000, 1.5, "multiply")))
print("365 / 5 = " + str(calculate(365, 5, "divide")))
print("5 % 2 = " + str(calculate(5, 2, "quotient")))
print("Invalid function call: " + calculate(100, 100, "foo"))

print("---------------------------")

list_temp = [1, 2, 5, 80, 2, -1, 100000]

def minimum(list):
    return min(list)

print("The minimum value in " + str(list_temp) + " is: " + str(min(list_temp)))
