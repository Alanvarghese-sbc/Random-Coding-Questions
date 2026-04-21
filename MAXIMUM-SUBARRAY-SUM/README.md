# 🔴 Maximum Subarray Sum (Kadane's Algorithm)

## 📌 Problem Statement

Given an array of integers (both positive and negative), find the **maximum sum of a contiguous subarray** and print the subarray.

---

## 🎯 Objective

* Identify a **continuous subarray**
* Such that its **sum is maximum**
* Also print the elements of that subarray

---

## 🧠 Approach / Logic

This problem is solved using **Kadane’s Algorithm**.

### Key Idea:

At each element, decide:

* Start a **new subarray**
* OR continue the **existing subarray**

---

## ⚙️ Algorithm Steps

1. Initialize:

   * `current_sum` = first element
   * `max_sum` = first element

2. Traverse the array:

   * If current element is greater than (current_sum + element)
     → start new subarray
   * Else
     → continue adding

3. Track:

   * Maximum sum
   * Start and end indices

---

## 💻 Python Implementation

```python
n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]

start = 0
end = 0
temp_start = 0

for i in range(1, n):
    if arr[i] > current_sum + arr[i]:
        current_sum = arr[i]
        temp_start = i
    else:
        current_sum += arr[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

print(max_sum)
print("Subarray:", *arr[start:end+1])
```

---

## 📌 Example

### Input

```
8
-2 -3 4 -1 -2 1 5 -3
```

### Output

```
7
Subarray: 4 -1 -2 1 5
```

---

## ⚠️ Edge Cases

* All elements negative → return largest element
* Single element array
* Large inputs

---

## ⏱️ Complexity

* Time Complexity: **O(n)**
* Space Complexity: **O(1)**

---

## 🏆 Key Concepts Used

* Dynamic Programming (Kadane’s Algorithm)
* Array Traversal
* Greedy Decision Making

---

## 🚀 Learning Outcome

* Learn how to optimize subarray problems
* Understand decision-based iteration
* Build strong foundation for DSA interviews

---

## 📂 Tags

`#TCS-NQT` `#Kadane` `#Arrays` `#DynamicProgramming` `#Python`
