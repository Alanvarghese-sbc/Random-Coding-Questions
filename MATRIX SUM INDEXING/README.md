# 🔴 Matrix Sum Indexing (2D Arrays + Input Handling)

## 📌 Problem Statement

You are given:

* Two matrices **A** and **B** of size `n x m`
* `k` positions `(i, j)`

👉 Task:
For each position `(i, j)`, calculate:

```
A[i][j] + B[i][j]
```

👉 Print the **total sum** of all such values.

---

## 🎯 Objective

* Work with **2D arrays (matrices)**
* Handle **index-based access**
* Process multiple inputs dynamically

---

## 🧠 Key Concept

👉 `k` represents the **number of positions** you need to process.

For each position:

* Extract value from matrix A
* Extract value from matrix B
* Add both to total

---

## ⚙️ Algorithm Steps

1. Read `n` and `m`
2. Read matrix **A**
3. Read matrix **B**
4. Read `k` (number of positions)
5. Loop `k` times:

   * Read `(i, j)`
   * Add `A[i][j] + B[i][j]` to total
6. Print final total

---

## 💻 Python Code

```python
# Read matrix size
n, m = map(int, input().split())

# Read matrix A
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

# Read matrix B
B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

# Number of positions
k = int(input())

total = 0

for _ in range(k):
    i, j = map(int, input().split())
    
    # Add values from both matrices
    total += A[i][j] + B[i][j]

print(total)
```

---

## 📌 Example

### Input

```
2 2
1 2
3 4
5 6
7 8
2
0 0
1 1
```

### Output

```
18
```

---

## 🔍 Explanation

```
A[0][0] + B[0][0] = 1 + 5 = 6
A[1][1] + B[1][1] = 4 + 8 = 12

Total = 6 + 12 = 18
```

---

## ⚠️ Important Points

* Indexing starts from **0**
* Ensure `(i, j)` is within bounds
* Input format must be handled correctly
* Both matrices must be of same size `n x m`

---

## ⏱️ Complexity

* Time Complexity: **O(n × m + k)**
* Space Complexity: **O(n × m)**

---

## 🏆 Concepts Used

* 2D Arrays (Matrix)
* Indexing
* Looping
* Input parsing
* Basic arithmetic

---

## 🚀 Learning Outcome

* Understand matrix input handling
* Learn index-based operations
* Improve logic for scenario-based problems

---

## 📂 Tags

`#TCS-NQT` `#Matrix` `#2D-Array` `#Indexing` `#Python`
