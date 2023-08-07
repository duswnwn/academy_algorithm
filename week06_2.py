array = input()
stack = []
for elem in array:
    if elem == '(':
        stack.append(elem)
    else:
        if len(stack) == 0 :
            print("NO")
            break
        elif stack[len(stack)-1] == '(':
            stack.pop()
            continue
        else:
            print("NO")
            break
else:
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')