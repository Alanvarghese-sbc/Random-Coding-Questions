# 🔴 Typewriter Problem (String + Stack)

## 📌 Problem Statement

Given two strings, determine whether they are equal after processing backspace characters.

* The character `#` represents a **backspace**
* When `#` is encountered, the previous character is removed

---

## 🎯 Objective

* Process both strings after applying backspaces
* Compare the final strings
* Return **True** if equal, otherwise **False**

---

## 🧠 Approach / Logic

This problem is solved using a **Stack-based approach**.

### Key Idea:

* Traverse each string
* Push characters into a stack
* If `#` is found → pop last character (if any)
* Convert stack back to string

---

## ⚙️ Algorithm Steps

1. Create a helper function to process a string
2. Initialize an empty stack
3. Traverse each character:

   * If character is `#` → pop from stack
   * Else → push character
4. Convert stack to string
5. Compare processed results of both strings

---

## 💻 Python Implementation

```python
def process(s):
    stack = []

    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


s1 = input().strip()
s2 = input().strip()

if process(s1) == process(s2):
    print("True")
else:
    print("False")
```

---

## 📌 Example 1

### Input

```
ab#c
ad#c
```

### Output

```
True
```

### Explanation

```
"ab#c" → "ac"
"ad#c" → "ac"
```

---

## 📌 Example 2

### Input

```
a##c
#a#c
```

### Output

```
True
```

---

## ⚠️ Edge Cases

* String starts with `#`
* Multiple consecutive `###`
* Resulting string becomes empty

---

## ⏱️ Complexity

* Time Complexity: **O(n)**
* Space Complexity: **O(n)** (stack)

---

## 🏆 Key Concepts Used

* Stack (LIFO)
* String Traversal
* Simulation

---

## 🚀 Learning Outcome

* Understand stack-based string processing
* Learn to simulate real-world operations (like backspace)
* Improve problem-solving for string manipulation

---

## 📂 Tags

`#TCS-NQT` `#Stack` `#Strings` `#Python` `#Simulation`
