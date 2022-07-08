# 12-5. 뱀

n = int(input('n = '))    # 보드의 크기
k = int(input('k = '))    # 사과의 개수

# 사과의 위치
data = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input('l = '))    # 뱀의 방향 변환 횟수

l_list = []
for _ in range(l):
    tmp = input('l -> ')
    l_list.append([int(tmp.split()[0]), tmp.split()[1]])

######################################################################################

x, y = 1, 1     # 뱀의 초기 위치

# 방향 설정
dir = ['L', 'D']