threshold = 100
count = 0

for i in range(7):
    unit = int(input("Enter units: "))

    if unit > threshold:
        count += 1

print("Days Crossed =", count)