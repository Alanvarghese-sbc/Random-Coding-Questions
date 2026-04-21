# 🔴 Fraud Transaction Detection (Hash Map Approach)

## 📌 Problem Statement

Given a list of transaction records, identify **duplicate (fraudulent) transactions** that occur within **60 seconds**.

Each transaction contains:

```
Sender Receiver Amount Timestamp
```

---

## 🎯 Objective

* Detect transactions with:

  * Same **Sender**
  * Same **Receiver**
  * Same **Amount**
* AND time difference ≤ **60 seconds**

---

## 🧠 Approach / Logic

This problem is solved using a **Hash Map (Dictionary)**.

### Key Idea:

* Store previously seen transactions
* Use a combination of `(sender, receiver, amount)` as a unique key
* Compare timestamps to detect fraud

---

## ⚙️ Algorithm Steps

1. Read all transactions
2. Create a dictionary:

   ```
   key → last timestamp
   ```
3. For each transaction:

   * If key already exists:
    * Check time difference ≤ 60 → fraud
    * Update latest timestamp

---

## 💻 Python Implementation

```python
n = int(input())

transactions = []
for _ in range(n):
    sender, receiver, amount, time = input().split()
    transactions.append((sender, receiver, amount, int(time)))

seen = {}
fraud_count = 0

for sender, receiver, amount, time in transactions:
    key = (sender, receiver, amount)

    if key in seen:
        if abs(time - seen[key]) <= 60:
            fraud_count += 1

    # Update latest timestamp
    seen[key] = time

print("Fraud Transactions Found:", fraud_count)
```

---

## 📌 Example

### Input

```
3
A B 100 1000
A B 100 1050
A B 200 2000
```

### Output

```
Fraud Transactions Found: 1
```

### Explanation

* First and second transactions are identical
* Time difference = 50 seconds (≤ 60)
* Hence, fraud detected

---

## ⚠️ Edge Cases

* No duplicate transactions → output `0`
* Transactions with same data but time difference > 60 → not fraud
* Multiple frauds for same key

---

## ⏱️ Complexity

* Time Complexity: **O(n)**
* Space Complexity: **O(n)**

---

## 🏆 Key Concepts Used

* Hash Map (Dictionary)
* Tuple as Key
* Time-based comparison

---

## 🚀 Learning Outcome

* Learn how hashing helps in fast lookup
* Understand real-world scenario problem solving
* Improve data structure usage

---

## 📂 Tags

`#TCS-NQT` `#HashMap` `#Python` `#RealWorldProblem` `#DSA`
