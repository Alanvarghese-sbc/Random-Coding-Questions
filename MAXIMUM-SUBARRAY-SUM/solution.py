n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]

start = 0
end = 0
temp_start = 0

for i in range(1, n ):
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
print(*arr[start:end+1])
