# 13-4. 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

# p = "(()())()"
# p = ")("
# p = "()))((()"

tmp = "()()))(("

from collections import deque

# 균형잡힌 괄호 문자열 확인
def balanced_str(p):
    check = 0
    for str in p:
        if str == "(":
            check += 1
        else:
            check -= 1

    if check == 0:
        return True
    else:
        return False

# 올바른 괄호 문자열 확인
def proper_str(p):
    check = 0
    for str in p:
        if str == "(":
            check += 1
        else:
            check -= 1

            if check < 0:
                return False

    return True

# "올바른 괄호 문자열"이 아닐 때 변환
def solution(result, p):
    print("------------solution (result : ", result, ", p : ", p, " ------------")

    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == "":
        result += p

    # Case1. "올바른 괄호 문자열"인 경우
    if proper_str(p) == True:
        print("1. 올바른 괄호 문자열")
        result += p

    # Case2. "올바른 괄호 문자열"이 아닌 경우
    else:
        print("2. 올바르지 않은 괄호 문자열")

        for num in range(1, len(p)):
            temp = p[0 : num + 1]

            if balanced_str(temp) == True:
                u = temp
                v = p[num + 1 : len(p)]
                break

        print("u : ", u, ", v : ", v)

        if proper_str(u) == True:
            result += u
            print("solution_result : ", result)
            solution(result, v)

        else:
            temp = "(" + u[1 : len(u) - 1] + ")"
            solution(result, temp)
            # print("temp : ", temp)

    return result


result = ""

# ()()))((
print("\n>>>>>>>>> input : ", tmp, ", result : ", solution(result, tmp))
