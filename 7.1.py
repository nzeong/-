import sys
# sys.stdin = open("input.txt", "r")

def DFS(v, sum, t):
    global max
    if t > m:
        return
    if v == n+1:    
        if max <= sum:
            max = sum
    else:
        DFS(v+1, sum + a[v][0], t + a[v][1])
        DFS(v+1, sum, t)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    a.append((0, 0))
    for _ in range(n):
        p, q = map(int, input().split())
        a.append((p, q))
    max = 0
    DFS(1, 0, 0)
    print(max)
    