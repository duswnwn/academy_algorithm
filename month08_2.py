a, b = map(int, input().strip().split(' '))
nums = list(map(int,input().split()))
m,temp = sum(nums[0:b]),sum(nums[0:b])
for i in range(1,a-b+1):
    temp = temp + nums[i+b-1] - nums[i-1]
    if nums[i+b-1] < nums[i-1]:
        continue
    else:
        m = max(temp, m)

print(m)