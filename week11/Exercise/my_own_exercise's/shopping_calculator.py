total = 0
while True:
    price = float(input("Price:"))
    if total + price > 10:
        print(total)
        break

    total += price
