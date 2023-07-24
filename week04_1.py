world = input()

count = 0
for elem in world:
    if elem == "#":
        count += 1
        if count > 1 :
            break
    else:
        continue

if count > 1:
    print("NO")
else:
    print("YES")