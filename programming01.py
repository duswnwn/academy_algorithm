def solution(s):
    stack = []
    for elem in s:
        if elem == '(':
            stack.append(elem)
        elif len(stack) > 0 and elem == ')':
            stack.pop()
        else:
            return False

    if len(stack) == 0:
        answer = True
    else:
        answer = False
    return answer

if __name__ == '__main__':
    solution(input())