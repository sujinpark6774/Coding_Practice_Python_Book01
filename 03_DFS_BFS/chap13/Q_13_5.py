# 13-5. 연산자 끼워 넣기

# 2
# 5 6
# 0 0 1 0

# 3
# 3 4 5
# 1 0 1 0

# 6
# 1 2 3 4 5 6
# 2 1 1 1

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

# 연산 개수 (덧셈, 뺄셈, 곱셈, 나눗셈)
cnt = list(map(int, input().split()))
operation = ["+", "-", "*", "/"]

operations = []
for i in range(4):
    operations += list(operation[i] * cnt[i])

cases = list(permutations(operations, n - 1))

val_min = 1e9
val_max = -1e9

for case in cases:
    answer = a[0]
    for num in range(len(case)):
        if case[num] == "+":
            answer += a[num + 1]
        elif case[num] == "-":
            answer -= a[num + 1]
        elif case[num] == "*":
            answer *= a[num + 1]
        elif case[num] == "/":
            answer //= a[num + 1]

    print("case : ", case, "case[num] : ", case[num], ", answer : ", answer)

    val_min = min(val_min, answer)
    val_max = max(val_max, answer)

print(val_max, val_min)


