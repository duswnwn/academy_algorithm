n, m = map(int,input().split())

nums = [i+1 for i in range(n)]

for _ in range(m):
    u, v = map(int,input().split())
    temp = nums[u-1]
    nums[u-1] = nums[v-1]
    nums[v-1] = temp

print(*nums)