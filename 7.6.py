import sys
sys.stdin = open("input.txt", "r")

def DFS(v, p):
    global cnt
    if v == n:
        for k in range(p):
            print(chr(res[k]+64), end='')
        cnt += 1
        print()
    else:
        for i in range(1, 27):
            if arr[v] == i: 
                res[p] = i
                DFS(v+1, p+1)
            elif (10*arr[v]+arr[v+1]) == i:
                res[p] = i
                DFS(v+2, p+1)
    
if __name__ == '__main__':
    arr = list(map(int, input()))
    n = len(arr)
    res = [0]*n
    arr.insert(n, -1)
    cnt = 0
    DFS(0, 0)
    print(cnt)