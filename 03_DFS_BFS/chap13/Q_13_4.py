# 13-4. 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

p = "(()())()"
# p = ")("
# p = "()))((()"

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
def solution(p):

    result = ""

    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == "":
        return result

    for num in range(1, len(p)):
        u = p[0 : num + 1]
        v = p[num + 1 : len(p) + 1]
        if balanced_str(u) == True:
            break

    if proper_str(u) == True:
        result = u + solution(v)

    else:
        result = "(" + solution(v) + ")"

        temp_u = ""
        for i in u[1 : -1]:
            if i == ")":
                temp_u += "("
            else:
                temp_u += ")"

        result += temp_u

    return result

print("\n>>>>>>>>> input : ", p, ", result : ", solution(p))
