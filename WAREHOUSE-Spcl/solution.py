# n = int(input())
# if n <= 0:
#     print(0)
#     exit()

# spcl_count = 0

# arr = {}
# for i in range(1,n+1):
#     arr[i] = range(i, n+1)

# for i in arr:
#     for j in arr[i]:
#         if (i + j) % 2 == 0:
#             spcl_count += 1

# print(spcl_count)
            
#  or

n = int(input())
if n <= 0:
    print(0)
    exit()
spcl_count = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if (i + j) % 2 == 0:
            spcl_count += 1
print(spcl_count)

