t = int(input())

for _ in range(t): # 테스트 케이스 수 만큼 반복
    n = int(input())
    nums = list(map(int,input().split()))
    ans = 0

    for i in range(n):
        if i == n-1:
            break
        elif nums[i] != nums[i+1]:
            if i == 0:
                if nums[i] == nums[i+2]:
                    print(i+2)
                    break
                else:
                    print(i+1)
                    break
            else:
                if nums[i] == nums[i-1]:
                    print(i+2)
                    break
                else:
                    print(i+1)
                    break
        else:
            continue

