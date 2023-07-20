S = list(input())
T = input()

for elem in T:
    if elem in S:
        S.remove(elem)
    else:
        break

if len(S):
    print("NO")
else:
    print("YES")
