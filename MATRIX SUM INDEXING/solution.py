n,m = map(int, input().split())

A = []

for _ in range(n):
    A.append(list(map(int, input().split())))

B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

k = int(input())

total = 0
for _ in range(k):
    i, j = map(int, input().split())
    total += A[i][j] + B[i][j]

print(total)