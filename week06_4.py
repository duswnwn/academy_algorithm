from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    put = input()
    if " " in put:
        a, b = map(int, put.split())
    else:
        a = int(put)
    if a == 1:
        d.appendleft(b)
    elif a == 2:
        d.append(b)
    elif a == 3:
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif a == 4:
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif a == 5:
        print(len(d))
    elif a == 6:
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif a == 7:
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif a == 8:
        if len(d) == 0:
            print(-1)
        else:
            print(d[len(d) - 1])
