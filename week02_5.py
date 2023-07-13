t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    real = nums.copy()
    for _ in range(n-1):
        m = len(real)
        nums = real.copy()
        for i in range(m-1):
            if nums[i] > nums[i+1]:
                real.pop(i+1)
                break
    print(*real)