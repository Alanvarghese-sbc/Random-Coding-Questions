# 🔴 Range Filtering with Constraints (Math + String Logic)

## 📌 Problem Statement

Given a range `[start, end]`, print all numbers that satisfy the following conditions:

1. Divisible by **7**
2. NOT divisible by **5**
3. NOT a **palindrome**
4. NO **repeating digits**

If the range exceeds `10^6`, print `"Invalid Range"`.

---

## 🎯 Objective

Filter numbers based on multiple constraints and print valid results.

---

## 🧠 Approach / Logic

For each number in the range:

* Check divisibility conditions
* Check palindrome property
* Check for repeating digits using a set

---

## ⚙️ Algorithm Steps

1. Read `start` and `end`
2. If `end > 10^6` → print `"Invalid Range"`
3. Loop through each number:

   * Check divisible by 7
   * Check NOT divisible by 5
   * Check NOT palindrome
   * Check NO repeating digits
4. Store valid numbers
5. Print result

---

## 💻 Python Implementation

```python
start, end = map(int, input().split())

# Constraint check
if end > 10**6:
    print("Invalid Range")
    exit()

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def has_repeating_digits(n):
    s = str(n)
    return len(s) != len(set(s))

result = []

for num in range(start, end + 1):
    if (num % 7 == 0 and
        num % 5 != 0 and
        not is_palindrome(num) and
        not has_repeating_digits(num)):
        
        result.append(num)

# Output
if result:
    print(*result)
else:
    print("No valid numbers")
```

---

## 📌 Example

### Input

```
10 50
```

### Output

```
14 21 28 42 49
```

---

## 🔍 Key Logic Explained

### 🔸 Palindrome Check

```python
s == s[::-1]
```

### 🔸 Repeating Digits Check

```python
len(s) != len(set(s))
```

👉 If lengths differ → duplicates exist

---

## ⚠️ Edge Cases

* Range too large → `"Invalid Range"`
* No valid numbers → `"No valid numbers"`
* Single number input

---

## ⏱️ Complexity

* Time Complexity: **O(n × d)**
  (n = range size, d = number of digits)
* Space Complexity: **O(n)**

---

## 🏆 Key Concepts Used

* Modulo operations
* String manipulation
* Set (for duplicate detection)
* Filtering logic

---

## 🚀 Learning Outcome

* Combine multiple conditions in one problem
* Use sets for duplicate detection
* Improve logic-building skills

---

## 📂 Tags

`#TCS-NQT` `#MathLogic` `#Strings` `#Sets` `#Filtering` `#Python`
