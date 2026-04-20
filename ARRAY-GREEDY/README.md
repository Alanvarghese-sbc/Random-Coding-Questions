# 🧩 Maximum Elements with Sum ≤ X (Greedy Approach)

## 📌 Problem Statement

Given an array of integers and a target value `X`, find the **maximum number of elements** that can be selected such that their **sum does not exceed X**.

---

## 🎯 Objective

* Maximize the **count of elements**
* Ensure the **sum of selected elements ≤ X**

---

## 🧠 Approach / Logic

This problem follows a **Greedy Strategy**:

1. Sort the array in ascending order
2. Start picking the smallest elements first
3. Keep adding elements until the sum exceeds `X`
4. Count how many elements were successfully added

👉 Why this works:

* Smaller elements allow us to include more numbers within the limit
* Choosing larger elements first would reduce the count

---

## 💻 Python Implementation

```python
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Edge case
if n <= 0:
    print(0)
    exit()

# Step 1: Sort the array
arr.sort()

count = 0
current_sum = 0

# Step 2: Greedy selection
for i in arr:
    if current_sum + i <= x:
        current_sum += i
        count += 1
    else:
        break

# Output result
print(count)
```

---

## 📌 Example

### Input

```
4
4 2 1 10
7
```

### Output

```
3
```

### Explanation

Sorted array → `[1, 2, 4, 10]`
Selected elements → `1 + 2 + 4 = 7`
Total count → **3**

---

## ⚠️ Edge Cases

* Empty array → Output `0`
* All elements greater than `X` → Output `0`
* Negative values → typically not considered (based on constraints)

---

## 🏆 Key Concepts Used

* Greedy Algorithm
* Sorting
* Iterative traversal

---

## 🚀 Learning Outcome

* Understand how greedy algorithms work
* Learn to optimize for **maximum count under constraint**
* Improve problem-solving for real-world scenarios

---

## 📂 Tags

`#TCS-NQT` `#Greedy` `#Arrays` `#Python` `#Sorting` `#LogicBuilding`
