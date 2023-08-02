n = int(input())      

data = list(map(int, input().split()))

sum = [0] * n
sum[0] = data[0]

# Summing the maximum intervals of a given sequence
for i in range(1, n):
    sum[i] = max(sum[i-1] + data[i], data[i])

print(max(sum))
