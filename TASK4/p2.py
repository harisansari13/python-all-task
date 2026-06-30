n = int(input("Enter number of transactions: "))

deposit = 0
withdrawal = 0

for i in range(n):
    t = input("deposit/withdrawal: ")

    if t.lower() == "deposit":
        deposit += 1
    else:
        withdrawal += 1

print("Deposits =", deposit)
print("Withdrawals =", withdrawal)