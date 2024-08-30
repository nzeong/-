import sys
sys.stdin = open("input.txt", "r")

def DFS(v, sum):
    global max
    if v == n+1:
        if sum > max:
            max = sum
    else:
        if v+a[v][0] <= n+1:
            DFS(v+a[v][0], sum+a[v][1])
        DFS(v+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = []
    a.append((0,0))
    for _ in range(n):
        p, q = map(int, input().split())
        a.append((p, q))
    max = 0
    DFS(1, 0)
    print(max)