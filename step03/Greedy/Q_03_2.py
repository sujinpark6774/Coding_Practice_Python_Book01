# 03-2. 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해져야 하는 횟수 계산
# (가장 큰 수의 m-1 반복 + 두 번째로 큰 수)이어야 하므로 k+1로 나눔
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)