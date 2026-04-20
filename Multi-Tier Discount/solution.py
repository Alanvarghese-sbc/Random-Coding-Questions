amount = int(input())

if amount < 0:
    print("Error")
else:
    if amount <= 1000:
        discount = 0.05
    elif amount <= 5000:
        discount = 0.1
    elif amount > 5000:
        discount = 0.15

final_price = amount - (amount * discount)
print(int(final_price))