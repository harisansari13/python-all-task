highest = -999

for i in range(7):
    temp = int(input("Enter temperature: "))

    if temp > highest:
        highest = temp

print("Highest Temperature =", highest)