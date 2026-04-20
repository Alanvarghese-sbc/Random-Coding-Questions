n = int(input())
arr = list(map(int, input().split()))
x = int(input())

if n <= 0:
    print(0)
    exit()

arr.sort()

count = 0
current_sum = 0

for i in arr:
    if current_sum + i <= x:
        current_sum += i
        count += 1
    else:
        break

print(count)
