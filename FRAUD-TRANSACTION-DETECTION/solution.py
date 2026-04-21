n  = int(input())
transaction = []
for _ in range(n):
    sender, receiver, amount, time = input().split()
    transaction.append((sender, receiver, amount, int(time)))

seen = {}
fraud_count = 0
for sender, receiver, amount, time in transaction:
    key = (sender, receiver, amount)

    if key in seen :
        if abs(time - seen[key]) <= 60:
            fraud_count += 1
    seen[key] = time

print(fraud_count)