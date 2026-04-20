# 🧩 Multi-Tier Discount Problem (TCS NQT Practice)

## 📌 Problem Statement

A shop provides discounts based on the total bill amount:

* ₹0 – ₹1000 → **5% discount**
* ₹1001 – ₹5000 → **10% discount**
* Above ₹5000 → **15% discount**
* If the amount is negative → print **"Error"**

---

## 🎯 Objective

* Take input amount from user
* Apply the correct discount
* Print the **final price after discount**
* Handle invalid input properly

---

## 🧠 Approach / Logic

1. Read the input amount
2. Check if the amount is negative

   * If yes → print `"Error"`
3. Otherwise:

   * Use `if-elif-else` to determine discount rate
   * Calculate discount using:

     ```
     discount_amount = amount * discount_rate
     ```
   * Calculate final price:

     ```
     final_price = amount - discount_amount
     ```
4. Print the final price

---

## 💻 Python Implementation

```python
# Take input
amount = int(input())

# Check for invalid input
if amount < 0:
    print("Error")
else:
    # Apply discount based on range
    if amount <= 1000:
        discount = 0.05
    elif amount <= 5000:
        discount = 0.10
    else:
        discount = 0.15

    # Calculate final price
    final_price = amount - (amount * discount)

    # Print result
    print(int(final_price))
```

---

## 📌 Example

### Input

```
1200
```

### Output

```
1080
```

---

## ⚠️ Edge Cases

* Negative input → `"Error"`
* Input = 0 → Output = 0
* Large values → should still work correctly

---

## 🏆 Key Concepts Used

* Conditional statements (`if-elif-else`)
* Basic arithmetic operations
* Input validation

---

## 🚀 Learning Outcome

This problem helps in understanding:

* Decision-making logic
* Writing clean and structured code
* Handling real-world billing scenarios

---

## 📂 Tags

`#TCS-NQT` `#Python` `#Beginner` `#IfElse` `#LogicBuilding`
