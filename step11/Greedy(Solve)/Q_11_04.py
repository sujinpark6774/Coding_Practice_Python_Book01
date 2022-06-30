# 11-04. 만들 수 없는 금액

n = int(input())
coin_type = list(map(int, input().split()))
coin_type.sort()

target = 1
for x in coin_type:
    if target < x:
        break
    target += x

print(target)