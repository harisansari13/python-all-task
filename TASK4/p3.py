n = int(input("Enter total seats: "))
reserved = [2, 5, 8]

for seat in range(1, n + 1):
    if seat not in reserved:
        print(seat)