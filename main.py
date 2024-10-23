a = 12345
b = str(a)

def DFS(L, sum):
    if L == len(b):
        print(sum)
        return
    else:
        DFS(L+1, sum+ b[L])
        DFS(L+1, sum)

print(DFS(0,""))