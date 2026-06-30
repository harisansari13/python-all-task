age = int(input("Enter age: "))
fitness = input("Fit? (yes/no): ")

if age >= 18:
    if fitness.lower() == "yes":
        print("Mission Accepted")
    else:
        print("Fitness Test Failed")
else:
    print("Too Young")