s = list(input())
t = input()

i = 0
count = 0
for elem in s:
    if i < len(t) and elem == t[i]:
        count += 1
        i += 1
    else:
        continue

if len(t) == count:
    print("YES")
else:
    print("NO")

