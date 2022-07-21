# 12-8. 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations

# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
# result = 2
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
# result = 1

def solution(n, weak, dist):
    # 원형으로 주어진 값을 일자로 쭉 핀다고 생각 -> 리스트 길이를 2배로 늘림
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1      # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1 로 초기화 (굳이 1e9로 할 필요없음)

    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인

        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구의 수

            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]

            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구를 투입
                    if count > len(dist):  # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)  # 최솟값 계산

    if answer > len(dist):
        return -1
    return answer

print(solution(n, weak, dist))