# 🔴 Population State Transition (DP + Probability)

## 📌 Problem Statement

You are given:

* Initial number of **Happy people (H)**
* Initial number of **Sad people (S)**

### Rules (per operation):

* **Happy → 70% become Sad**
* **Sad → 50% become Happy**

👉 Perform **4 operations**

👉 Find the final number of:

* Happy people
* Sad people

---

## 🎯 Objective

Simulate transitions between two states using probability rules.

---

## 🧠 Key Concept

At each step:

```
New Happy = 50% of Sad
New Sad = 70% of Happy
```

👉 Values are updated **simultaneously per iteration**

---

## ⚙️ Algorithm Steps

1. Read initial values of `happy` and `sad`
2. Repeat for 4 iterations:

   * Calculate new values
   * Update both variables
3. Print final results

---

## 💻 Python Implementation

```python
happy = float(input())
sad = float(input())

for _ in range(4):
    new_happy = 0.5 * sad
    new_sad = 0.7 * happy
    
    happy = new_happy
    sad = new_sad

print("Happy =", round(happy, 2))
print("Sad =", round(sad, 2))
```

---

## 📌 Example

### Input

```
100
0
```

### Output

```
Happy = 12.25
Sad = 0.0
```

---

## 🔍 Step-by-Step

| Iteration | Happy | Sad  |
| --------- | ----- | ---- |
| Start     | 100   | 0    |
| 1         | 0     | 70   |
| 2         | 35    | 0    |
| 3         | 0     | 24.5 |
| 4         | 12.25 | 0    |

---

## ⚠️ Important Points

* Use **temporary variables** (`new_happy`, `new_sad`)
* Update both values **after calculation**
* Use `float` for precision
* Round output if required

---

## ⏱️ Complexity

* Time Complexity: **O(1)** (fixed 4 iterations)
* Space Complexity: **O(1)**

---

## 🏆 Concepts Used

* Iteration
* Probability
* State Transition
* Dynamic Programming (basic)

---

## 🚀 Learning Outcome

* Understand state transitions
* Work with probabilities
* Avoid update mistakes using temp variables

---

## 📂 Tags

`#TCS-NQT` `#DP` `#Probability` `#Simulation` `#Python`
