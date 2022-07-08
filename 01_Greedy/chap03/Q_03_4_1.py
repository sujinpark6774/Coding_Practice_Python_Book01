# 03-4. 1이 될 때까지
import time

n, k = map(int, input().split())

answer = 0

while(n != 1):
    if (n % k == 0):
        n = n / k
        answer += 1
    else:
        n = n - 1
        answer += 1

print(answer)