# Problem 1: Print 1 to N

# Take N from user and print numbers from 1 to N.
num = int(input("Enter the limit :"))
for i in range(1,num+1):
    print(i)

# Problem 2: Sum of Numbers

# Take N and print sum from 1 to N.
sum = 0
for i in range(1,num+1):
    sum = sum+i

print(f"The sum of numbers from 1 to {num} is {sum}")

# Problem 3: Sum of Digits

num2 = int(input("Enter the number :"))
sum1=0
while num2>0:
    rem = num2%10
    sum1 = sum1+rem
    num2 = num2//10
print(f"The sum of digits is {sum1}")

# Problem 4: Reverse a Number

num3 = int(input("Enter the number :"))
reverse = 0
while num3>0:
    rem = num3%10
    reverse = reverse*10+rem
    num3 = num3//10
print(f"The reverse of the number is {reverse}")

# Problem 5: Count Digits
num4 = int(input("Enter the number :"))
count = 0
while num4>0:
    num4 = num4//10
    count = count+1
print(f"The number of digits is {count}")

# Problem 6: Palindrome Number
num5 = int(input("Enter the number :"))
temp = num5
reverse1 = 0
while num5>0:
    rem = num5%10
    reverse1 = reverse1*10+rem
    num5 = num5//10
if temp == reverse1:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")


# Problem 7: Prime Number

# Check if a number is prime.

# (Hint: loop from 2 to n-1)

num6 = int(input("Enter the number :"))




