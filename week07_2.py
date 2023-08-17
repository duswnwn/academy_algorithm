book = input()

m = int(input())
leftPage = [book[0]]
rightPage = []
for elem in range(len(book) - 1, 0, -1):
    rightPage.append(book[elem])

for _ in range(m):
    action = input()

    if action == 'prev':
        if len(leftPage) == 1:
            continue
        else:
            rightPage.append(leftPage.pop())
    elif action == 'next':
        if len(rightPage) == 1:
            continue
        else:
            leftPage.append(rightPage.pop())
    elif action == 'left':
        if len(leftPage) == 1:
            continue
        else:
            leftPage.pop()
    elif action == 'right':
        if len(rightPage) == 1:
            continue
        else:
            rightPage.pop()

print(leftPage[len(leftPage) - 1], rightPage[len(rightPage) - 1])