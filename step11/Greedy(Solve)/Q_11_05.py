# 11-05. 볼링공 고르기

n, m = map(int, input().split())
k = list(map(int, input().split()))

count = 0
for i in range(n-1):
    for j in range(i, n):
        if k[i] != k[j]:
            count += 1

print(count)