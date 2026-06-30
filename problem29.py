balance = 5000

amount = int(input("Enter amount: "))

if amount <= balance:
    balance -= amount
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")