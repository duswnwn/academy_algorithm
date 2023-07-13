t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        nums[u-1] -= 1
        nums[v-1] += 1
    print(*nums)