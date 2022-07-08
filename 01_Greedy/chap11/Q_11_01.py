# 11-01. 모험가 길드

n = map(int, input().split())
x = list(map(int, input().split()))
x.sort()        # 1 2 2 2 3

group = 0       # 그룹 수
count = 0       # 그룹에 포함된 사람 수

for i in x:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)