amount = float(input("Enter shopping amount: "))

if amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

print("Final Amount =", amount - discount)