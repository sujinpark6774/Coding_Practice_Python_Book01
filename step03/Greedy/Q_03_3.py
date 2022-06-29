# 03-3. 숫자 카드 게임

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)