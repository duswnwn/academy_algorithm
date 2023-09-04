n, m = map(int, input().split())

nums = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    if nums[u - 1][v - 1] != 1:
        nums[u - 1][v - 1] = 1
        nums[v - 1][u - 1] = 1

for elems in nums:
    print(*elems)