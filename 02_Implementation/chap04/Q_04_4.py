# 04-4. 게임 개발

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]

x, y, dir = map(int, input().split())
d[x][y] = 1     # 현재 좌표 방문 처리

array = []      # 맵 정보
for i in range(n):
    array.append(list(map(int, input().split())))

#   0
# 3   1
#   2
# [북, 동, 남, 서] 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0
while True:
    # step1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    # step2-1. 회전한 이후에 정면에 가보지 않은 칸 또는 육지인 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1       # 방문한 칸으로 변경
        x, y = nx, ny       # 현재 위치 변경
        count += 1          # 움직인 횟수 + 1
        turn_time = 0       # 회전 수 초기화
        continue

    # step2-2. 회전한 이후에 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # step3. 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0       #회전 수 초기화

print(count)