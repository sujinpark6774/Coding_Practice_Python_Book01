# 11-03. 문자열 뒤집기

s = input()     # 0001100

count0 = 0      # 모두 0으로 바꾸는 경우 행동의 횟수
count1 = 0      # 모두 1으로 바꾸는 경우 행동의 횟수

if int(s[0]) == 1:
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):
    if int(s[i - 1]) != int(s[i]):
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))