from collections import deque
n = int(input())
q = deque()
for _ in range(n):
    i = input()
    if ' ' in i:
        a, b = map(int,i.split())
    else:
        a = int(i)
    if a == 1:
        q.append(b)
    elif a == 2:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif a == 3:
        print(len(q))
    elif a == 4:
        if len(q)== 0:
            print(1)
        else:
            print(0)
    elif a == 5:
        if len(q) != 0 :
            print(q[0])
        else:
            print(-1)