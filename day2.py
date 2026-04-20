# 🔹 Problem 1: Even or Odd

number = int(input("Enter a number:"))
if number % 2 ==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# 🔹 Problem 2: Largest of Two Numbers

# Take two numbers and print the largest.

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
else:
    print(f"{num2} is larger than {num1}")

# 🔹 Problem 3: Positive, Negative or Zero
# Take a number and print:
# Positive
# Negative
# Zero

num3 = int(input("Enter number 3:"))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")

if num3>0:
    print(f"{num3} is Positive")
elif num3<0:
    print(f"{num3} is Negative")
else:
    print(f"{num3} is Zero")

age = int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")