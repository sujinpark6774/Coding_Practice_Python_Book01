# 11-02. 곱하기 혹은 더하기

s = input()

result = int(s[0])
for i in range(1, len(s)):
    if result == 0:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)