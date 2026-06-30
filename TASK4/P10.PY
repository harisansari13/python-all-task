def delivery_charge(amount):
    if amount >= 500:
        return 0
    else:
        return 50

print(delivery_charge(300))