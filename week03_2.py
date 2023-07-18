s = input()
length = len(s)//2

for i in range(1, length+1):
    if s[i-1] == s[-i]:
        continue
    else:
        print("NO")
        break
else:
    print("YES")