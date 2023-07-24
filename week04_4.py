import sys
import math
from collections import deque

input = sys.stdin.readline

t = int(input())

for c in range(t):
    n, m = map(int, input().split())
    visited = [False] * (n + 1)

    world = input()
    junsik_atk, junsik_hp = map(int, input().split())
    monster_atk, monster_hp = map(int, input().split())
    if c != t - 1:
        blank = input()

    start = world.index("@")
    visited[start] = True
    queue = deque()

    queue.append((start, m))
    flag = "NO"
    while (len(queue)):
        (cur, cur_m) = queue.popleft()

        for i in [-1, 1]:
            next, next_m = cur + i, cur_m
            if next < 0 or next > n-1:
                continue
            if world[next] == "#":
                next_m -= 1
                if next_m < 0:
                    continue
            elif world[next] == "&":
                a = math.ceil(monster_hp / junsik_atk)
                b = math.ceil(junsik_hp / monster_atk)
                if a > b:
                    continue
            elif world[next] == "O":
                flag = "YES"
                break

            if not visited[next]:
                queue.append((next, next_m))
                visited[next] = True

    print(flag)


