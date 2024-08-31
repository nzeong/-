import sys
# sys.stdin = open("input.txt", "r")

def DFS(v, sum):
    global num
    if sum > t:
        return
    if v == k:
        if sum == t:
            num += 1
    else:
        for i in range(a[v][1] + 1):
            DFS(v+1, sum + (a[v][0]*i))

if __name__ == "__main__":
    t = int(input())
    k = int(input())
    a = list()
    for _ in range(k):
        p, q = map(int, input().split())
        a.append((p, q))
    num = 0
    DFS(0, 0)
    print(num)