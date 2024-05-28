# calculator

print("Welcome to the calculator")

num_1 = int(input("please enter your first number: "))
num_2 = int(input("Please enter your second number: "))
operation = str(input("please select operation : +, /, -, %, // "))
total = 0

if operation == '+':
        add= num_1 + num_2
        total = add
elif operation == '-':
        sub = num_1-num_2
        total = sub
elif operation == '*':
        mul = num_1 * num_2
        total = mul
elif operation == '/':
        div = num_1 / num_2
        total = div
else:
    print("Please enter right value: ")
    
print(total)

            



        


