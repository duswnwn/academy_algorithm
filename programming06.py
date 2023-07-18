def solution(tickets):
    answer = []

    check = [False] * len(tickets)

    def dfs(src, dest):
        if len(dest) == len(tickets) + 1:
            answer.append(dest)
            return

        for index, ticket in enumerate(tickets):
            if src == ticket[0] and check[index] is False:
                check[index] = True
                dfs(ticket[1], dest + [ticket[1]])
                check[index] = False

    dfs("ICN", ["ICN"])

    answer.sort()

    return answer[0]