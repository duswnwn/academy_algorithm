n = int(input())
data = input()
count = 0
left = []
right = []
for i in range(1, n):
    temp_count = 0
    left = []
    right = []
    for j in range(i):
        if data[j] in left:
            continue
        else:
            left.append(data[j])
            temp_count += 1
    for k in range(i, n):
        if data[k] in right:
            continue
        else:
            right.append(data[k])
            temp_count += 1
    count = max(count, temp_count)

print(count)