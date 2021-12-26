V = 4   # 顶点的个数
INF = 65535    # 设定一个最大值
P = [[0]*V for i in range(V)] # 记录各个顶点之间的最短路径
# 有向加权图中各个顶点之间的路径信息
graph = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
# 中序递归输出各个顶点之间最短路径的具体线路
def printPath(i,j):
    k = P[i][j]
    if k == 0:
        return;
    printPath(i , k)
    print("%d-" % (k + 1) , end='')
    printPath(k , j)
# 输出各个顶点之间的最短路径
def printMatrix(graph):
    for i in range(V):
        for j in range(V):
            if j == i:
                continue
            print("%d - %d: 最短路径为:"%(i + 1, j + 1) , end='')
            if graph[i][j] == INF:
                print("INF")
            else:
                print(graph[i][j] , end='')
                print("，依次经过：%d-"%(i+1) , end='')
                # 调用递归函数
                printPath(i , j)
                print(j + 1)
# 实现弗洛伊德算法,graph[][V] 为有向加权图
def floydWarshall(graph):
    # 遍历每个顶点，将其作为其它顶点之间的中间顶点，更新 graph 数组
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # 如果新的路径比之前记录的更短，则更新 graph 数组
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    # 记录此路径
                    P[i][j] = k
    # 输出各个顶点之间的最短路径
    printMatrix(graph)

floydWarshall(graph)