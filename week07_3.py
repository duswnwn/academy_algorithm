from collections import deque

n, m = map(int, input().split())

stone = deque()

for i in range(n):
    stone.append(i + 1)

for _ in range(m):
    num = int(input())
    if num == 1:
        stone.append(stone.popleft())
    else:
        if len(stone) == 1:
            continue
        else:
            stone.popleft()

print(stone[0])