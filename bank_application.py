def check_balance():
    global balance
    print("================================")
    print(f"Your current balance is {balance}")
    print("================================")
    balance = 0.0

def deposite(amount):
    global balance
    if amount > 0:
      balance += amount
      
      
    else:
      print("================================================")
      print("Invalid amount. Please enter a positive value.")
      print("================================================")

def withraw(amount):
    global balance
    if amount <= 0:
        print("================================")
        print("Invalid amount. Please enter a positive value.")
        print("================================")
    elif amount > balance:
        print("================================")
        print("Insufficient funds. Please enter a smaller amount.")
        print("================================")
    else:
        balance -= amount
        
balance = 0.0
print("================================")
print("welcome to urban bank")
print("================================")

while True:
    print("1.Check your balance")
    print("2.Deposite an amount")
    print("3.Withraw an amount")
    print("4.quite")
    choice = input("Enter your choice")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amt = float(input("Enter the amount to deposite"))
        deposite(amt)
        print("======================================")
        print(f"amount deposite successfully {amt}")
        print("======================================")
    elif choice == '3':
        amt = float(input("Enter the amount to withraw"))
        withraw(amt)
        print("======================================")
        print(f"amount withraw successfully {amt}")
        print("======================================")

    elif choice == '4':
        print("================================")
        print("Thankyou for banking with us")
        print("================================")
        break
    else:
        print("Invalid Choice")

        