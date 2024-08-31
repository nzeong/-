import sys
# sys.stdin = open("input.txt", "r")

def DFS(v, sum):
    if v == k:
        if 1 <= sum <= s:
            res.add(sum)
    else:
        DFS(v+1, sum + a[v])
        DFS(v+1, sum)
        DFS(v+1, sum - a[v])

if __name__ == "__main__":
    k = int(input())
    a = list(map(int, input().split()))
    res = set()
    s = sum(a)
    DFS(0, 0)
    print(s-len(res))
    