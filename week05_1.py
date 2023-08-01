n, m = map(int,input().split())

nums = list(map(int,input().split()))

for _ in range(m):
    a, b = map(int,input().split())
    print(sum(nums[a-1:b]))