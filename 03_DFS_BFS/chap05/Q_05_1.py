# 05-1. DFS 연습

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

def dfs(graph, v, visit):
    visit[v] = True

    print(v, end = " ")

    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

dfs(graph, 1, visit)