import math
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    for _ in range(n-1):
        for i in range(n-1):
            while nums[i] > nums[i+1]:
                nums[i] = math.floor(nums[i]/2)
    print(*nums)