import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0]*(n+1)
dy[1] = 1
max = 0 # 전체 최대값
for i in range(2, n+1):
    tmp = 0 # 작은 것들중에 최대값
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and tmp<dy[j]:
            tmp = dy[j]
    dy[i] = tmp + 1
    if max < dy[i]:
        max = dy[i]
print(max)