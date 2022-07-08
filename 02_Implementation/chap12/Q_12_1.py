# 12-1. 럭키 스트레이트

n = input()

num1, num2 = 0, 0

for i in range(1, len(n) + 1):
    if i <= len(n)/2:
        num1 += int(n[i-1])
    else:
        num2 += int(n[i-1])

if num1 == num2:
    print("LUCKY")
else:
    print("READY")