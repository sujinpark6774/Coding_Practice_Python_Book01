# 13-3. 경쟁적 전염

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2


from collections import deque

n, k = map(int, input().split())
graph = []          # 2차원 행렬 정보
data = []           # 바이러스 위치 정보
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
data = deque(data)                     # deque([(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)])

s, a, b = map(int, input().split())

# 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(num, time, x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if time > s:
            break



        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = num
            data.append((num, time + 1, nx, ny))

    return graph

while data:
    virus, time, x, y = data.popleft()
    bfs(virus, time, x, y)

print(graph)
print(a, b)
print(graph[a - 1][b - 1])





