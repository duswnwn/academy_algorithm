word = input()

for i in word:
    i = ord(i)
    if i < 96:
        i += 32
    else:
        i -= 32
    print(chr(i), end="")
