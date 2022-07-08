# 04-2. 시각

n = int(input())

cnt = 0
for time in range(n+1): # 시간
    for min in range(60):  # 분
       for sec in range(60):  # 초
            if '3' in str(time) + str(min) + str(sec):
                cnt += 1

print(cnt)