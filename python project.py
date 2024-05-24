
print("Welcome to the HDFC Bank Registration page")
name = str(input("please enter your name: "))
age = int(input("please enter you age: "))
nationality = str(input("Please enter your nationality: " ))
acc_type = str(input("please choose your account type: 'salary', 'savings': "))
# eligibity criteria
if age >=18 and nationality =="indian" and acc_type == 'salary':
    print(f"Hi {name}, You are eligible to open {acc_type} account in HDFC bank")
    print("Please fill the below mandatory details")
    income = int(input("please enter you anual income in lakhs"))
    if income >= 3:
        print("Congradulations, you can open platinum account in our bank")
elif age >=18 and nationality =="indian" and acc_type == "savings":
    print("Congradulations, you can open silvar account in our bank")
else:
    print(f"Sorry{name}, You are not eligible for to open an account in this bank")
