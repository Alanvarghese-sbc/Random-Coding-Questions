start, end = map(int, input().split())
if end > 10**6:
    print("invalid Range")
    exit()

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def has_repeating_digits(num):
    s = str(num)
    return len(set(s)) != len(s)


result = []
for num in range(start, end + 1):
    if (num % 7 == 0 and num % 5 != 0 and not is_palindrome(num) and not has_repeating_digits(num)):
        result.append(num)

if result:
    print(*result)
else:
    print("No numbers found")