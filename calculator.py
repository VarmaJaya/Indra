def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations = {
    "+":add,
    "-":sub, 
    "*":multiply, 
    "/":divide
    }

num1 = int(input("Please enter your first number: "))


for operation in operations:
    print(operation)

operation_symbol = input("please choose the operation_symobol from the above symbols: ")
num2 = int(input("Please enter your Second number: "))
calculation_function= operations[operation_symbol]
first_answer = calculation_function(a=num1, b=num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")
operation_symbol = input("please another operation : ")
num3 = int(input("Please enter another number: "))
calculation_function= operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

