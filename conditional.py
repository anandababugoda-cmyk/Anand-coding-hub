
# age calculation
'''age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")'''

# age calculation
'''age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")'''


# Student marks and grades
'''marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")'''

# Login validation
'''username = str(input("Enter username: "))
password = int(input("Enter password: "))

if username == "admin" and password == 1234:
    print("Login successful")
else:
    print("Invalid username or password")'''


# ATM withdrawal validation
balance = 5000
withdrawal_amount = int(input("Enter withdrawal amount: "))
if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print("Withdrawal successful. Remaining balance:", balance)
else:
    print("Insufficient balance")  
