import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    world = input().rstrip()
    blank = input()
    start = world.index("@")
    end = world.index("O")
    rock = world.index("G")
    up = 1 if start < rock else -1
    count = 0
    for i in range(start, rock, up):
        if world[i] == '#':
            count += 1
            if count > m:
                break
        else:
            continue
    if count <= m:
        print("YES")
    else:
        count = 0
        up = 1 if start < end else -1
        for i in range(start, end, up):
            if world[i] == '#':
                count += 1
                if count > m:
                    break
            else:
                continue

        if count > m:
            print("NO")
        else:
            print("YES")