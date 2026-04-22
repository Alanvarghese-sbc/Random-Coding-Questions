# 🌀 Spiral Matrix Traversal (Python)

## 📌 Problem Statement

Given an `n x m` matrix, print all elements in **spiral order**.

Spiral order means traversing the matrix in this pattern:

* Left → Right
* Top → Bottom
* Right → Left
* Bottom → Top
  (repeat until all elements are visited)

---

## 📥 Input Format

* First line: Two integers `n` and `m` (rows and columns)
* Next `n` lines: Each line contains `m` integers

---

## 📤 Output Format

* Print all elements in spiral order (space-separated)

---

## 🧾 Example

### Input:

```
3 3
1 2 3
4 5 6
7 8 9
```

### Output:

```
1 2 3 6 9 8 7 4 5
```

---

## 🧠 Approach

We use **boundary traversal** with 4 pointers:

* `top` → starting row
* `bottom` → ending row
* `left` → starting column
* `right` → ending column

### Steps:

1. Traverse from **left to right** → move `top` down
2. Traverse from **top to bottom** → move `right` left
3. Traverse from **right to left** → move `bottom` up
4. Traverse from **bottom to top** → move `left` right

Repeat until boundaries overlap.

---

## 💻 Python Code

```python
n, m = map(int, input().split())

matrix = []

# Input matrix
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

top = 0
bottom = n - 1
left = 0
right = m - 1

result = []

while top <= bottom and left <= right:

    # Left → Right
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # Top → Bottom
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    # Right → Left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # Bottom → Top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)
```

---

## ⏱ Time & Space Complexity

* **Time Complexity:** `O(n × m)`
* **Space Complexity:** `O(n × m)` (for result list)

---

## 🔥 Key Concepts

* Matrix traversal
* Boundary shrinking
* Loop control & conditions

---

## 💡 Tips (TCS NQT)

* Always remember **4-direction traversal**
* Carefully update boundaries after each loop
* Handle edge cases (`1 row` or `1 column`)

---

## 🚀 Related Problems

* Boundary Traversal of Matrix
* Diagonal Traversal
* Rotate Matrix 90°

---

## 📌 Author

Alan Varghese
