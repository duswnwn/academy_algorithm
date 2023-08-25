n, m, k = map(int, input().strip().split(' '))
nums = [0]
point = list(map(int,input().split()))
for elem in point:
    nums.append(elem)
check = [False for _ in range(n+1)]


temp = k
while(True):
    if check[temp]:
        print("NO")
        break
    else:
        if temp == m:
            print("YES")
            break
        else:
            check[temp] = True
            temp = nums[temp]
