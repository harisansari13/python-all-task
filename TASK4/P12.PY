try:
    a = int(input("Enter value: "))
    b = int(input("Enter value: "))

    print(a / b)
except ZeroDivisionError:
    print("Cannot Divide By Zero")