#
# Team Notes by Sujin
# ref. 이것이 취업을 위한 코딩 테스트다. (나동빈 저)
#

###################################################################################################################

#
# 2차원 리스트 90도 회전 (시계 방향)
#

def rotate_a_matrix_by_90_degree(a):
    # input -> a: 2차원 리스트
    n = len(a)      # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0]*n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result