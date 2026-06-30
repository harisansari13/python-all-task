try:
    seat = int(input("Enter seat number: "))

    if seat <= 0:
        raise ValueError

    print("Seat Booked")
except ValueError:
    print("Invalid Seat Number")