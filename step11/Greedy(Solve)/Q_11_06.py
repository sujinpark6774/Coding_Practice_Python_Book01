# 11-06. 무지의 먹방 라이브 (풀이 중)
# https://programmers.co.kr/learn/courses/30/lessons/42891

food_times = list(map(int, input().split()))
k = int(input())

turn = 0
while k >= 0:
    for i in range(len(food_times)):

        if food_times[i] > 0:
            k -= 1
            food_times[i] -= 1



print("while 밖: ", food_times)
print("i: ", turn)