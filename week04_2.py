import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    world = str(input()).rstrip()
    blank = input()
    start = world.index("@")
    end = world.index("O")
    up = 1
    if start > end:
        up = -1
    count = 0
    
    for i in range(start, end, up):
        if world[i] == "#":
            count += 1
            if count > m:
                break
        else:
            continue

    if count > m:
        print("NO")
    else:
        print("YES")
