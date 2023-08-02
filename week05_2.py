n = int(input())
nums = list(map(int,input().split()))
sum_array = [nums[0]]
print(sum_array[0], end = " ")
for i in range(1,n):
    sum_array.append(sum_array[i-1] + nums[i])
    print(sum_array[i], end = " ")