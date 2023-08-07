n = int(input())

stack = [] 

for _ in range(n):
    a = input()
    if " " in a:
        n, b = map(int,a.split())
    else:
        n = int(a)
    if n == 1:
        stack.append(b)
    elif n == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif n == 3:
        print(len(stack))
    elif n == 4: 
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif n == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])