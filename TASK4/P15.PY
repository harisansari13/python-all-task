try:
    age = int(input("Enter age: "))
    print("Age =", age)
except ValueError:
    print("Invalid Age")