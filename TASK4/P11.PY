try:
    amount = float(input("Enter amount: "))
    print("Payment Successful")
except ValueError:
    print("Invalid Amount")