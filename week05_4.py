n, m = map(int, input().split())    
data = input()

for i in range(m):
    a,b = map(int, input().split())
    count = 0
    for elem in range(a,b+1):
        if data[elem-1] == 'e':
            count += 1
        else:
            continue
    print(count)