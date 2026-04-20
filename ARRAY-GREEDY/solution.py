# n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
count = 0
sum = 0
for i in arr:
    if sum + i <= x:
        sum += i
        count += 1
    else:
        break
print(count)