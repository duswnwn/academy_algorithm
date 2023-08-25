put = list(input())
stack = []
YesOrNo = True

for elem in put:
    last = len(stack) - 1
    if elem == ')' or elem == '}' or elem == ']':
        if len(stack) == 0:
            YesOrNo = False
            break

        elif elem == ')':
            if stack[last] != '(':
                YesOrNo = False
                break
            else:
                stack.pop()

        elif elem == ']':
            if stack[last] != '[':
                YesOrNo = False
                break
            else:
                stack.pop()

        elif elem == '}':
            if stack[last] != '{':
                YesOrNo = False
                break
            else:
                stack.pop()
    else:
        stack.append(elem)


if YesOrNo and len(stack) == 0:
    print("YES")
else:
    print("NO")