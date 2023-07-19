string = input()
alphabet = []

for elem in string:
    if elem in alphabet:
        continue
    else:
        alphabet.append(elem)

if len(alphabet) == 26:
    print("YES")
else:
    print("NO")