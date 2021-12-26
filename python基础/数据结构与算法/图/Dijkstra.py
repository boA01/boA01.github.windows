'''
有一个分布式服务集群，集群内含有 N 个服务节点，分别标记为 1 到 N。
给予一个列表 times，表示消息从两个节点间有向传递需要的时间。 
times[i] = (s, d, t)，其中 s 表示发出消息的源节点，
d 表示接收到消息的目标节点， t  表示信息有向传递的时间。
现在 K 节点发送了一个信号，请问至少需要多少秒才能使所有的服务节点
都收到该消息？如果消息不能传递给集群内全部节点，则返回-1。

[[2,1,1],[2,3,1],[3,4,1]]
4
2

2

times = eval(input()) # [[源结点，目标结点，权],...]
N = int(input()) # 结点个数
K = int(input()) # 当前结点

A = [[] for _ in range(N+1)]

for s, d, t in times:
    A[s].append((d,t))

dis = [float("inf")]*(N+1)
dis[K] = 0

queue = [K]
while queue:
    s = queue.pop(0)
    for d, t in A[s]:
        if dis[d] > dis[s] + t:
            dis[d] = dis[s] + t 
            queue.append(d)
max_dis = max(dis[1:])
print(-1 if max_dis==float("inf") else max_dis)

'''

'''
输入图的顶点数和边数：7 9
输入各个顶点：0 1 2 3 4 5 6
输入各个边的数据：
0 1 2
0 2 6
1 3 5
2 3 8
3 5 15
3 4 10
4 5 6
4 6 2
5 6 6
'''
V = 20   #顶点的最大个数
INFINITY = 65535    #设定一个最大值
P = [0]*V  # 记录顶点 0 到各个顶点的最短的路径
D = [0]*V  # 记录顶点 0 到各个顶点的总权值

class MGraph:
    vexs = []*V   #存储图中顶点数据
    arcs = [[0]*V for i in range(V)]    #二维列表，记录顶点之间的关系
    vexnum = 0    #记录图的顶点数和弧（边）数
    arcnum = 0

G = MGraph()

#根据顶点本身数据，判断出顶点在二维数组中的位置
def LocateVex(G,v):
    #遍历一维数组，找到变量v
    for i in range(G.vexnum):
        if G.vexs[i] == v:
            break
    #如果找不到，输出提示语句，返回-1
    if i>G.vexnum:
        print("顶点输入有误")
        return -1
    return i

#构造无向有权图
def CreateDG(G):
    print("输入图的顶点数和边数：",end='')
    li = input().split()
    G.vexnum = int(li[0])
    G.arcnum = int(li[1])
    print("输入各个顶点：",end='')
    G.vexs = [int(i) for i in input().split()]
    for i in range(G.vexnum):
        for j in range(G.vexnum):
            G.arcs[i][j] = INFINITY
    print("输入各个边的数据:")
    for i in range(G.arcnum):
        li = input().split()
        v1 = int(li[0])
        v2 = int(li[1])
        w = int(li[2])
        n = LocateVex(G,v1)
        m = LocateVex(G,v2)
        if m == -1 or n == -1:
            return
        G.arcs[n][m] = w
        G.arcs[m][n] = w

CreateDG(G)
#迪杰斯特拉算法，v0表示有向网中起始点所在数组中的下标
def Dijkstra_minTree(G,v0,P,D):
    #为各个顶点配置一个标记值，用于确认该顶点是否已经找到最短路径
    final = [0]*V
    #对各数组进行初始化
    for i in range(G.vexnum):
        D[i] = G.arcs[v0][i]
    #由于以v0位下标的顶点为起始点，所以不用再判断
    D[v0] = 0
    final[v0] = 1
    k =0
    for i in range(G.vexnum):
        low = INFINITY
        #选择到各顶点权值最小的顶点，即为本次能确定最短路径的顶点
        for w in range(G.vexnum):
            if not final[w]:
                if D[w] < low:
                    k = w
                    low = D[w]
        #设置该顶点的标志位为1，避免下次重复判断
        final[k] = 1
        #对v0到各顶点的权值进行更新
        for w in range(G.vexnum):
            if not final[w] and (low + G.arcs[k][w]<D[w]):
                D[w] = low + G.arcs[k][w]
                P[w] = k   #记录各个最短路径上存在的顶点

Dijkstra_minTree(G,0,P,D)

print("最短路径为：")
for i in range(1,G.vexnum):
    print("%d - %d的最短路径中的顶点有："%(i,0),end='')
    print("%d-"%(i),end='')
    j = i
    #由于每一段最短路径上都记录着经过的顶点，所以采用嵌套的方式输出即可得到各个最短路径上的所有顶点
    while P[j] != 0:
        print("%d-"%(P[j]),end='')
        j = P[j]
    print("0")
print("源点到各顶点的最短路径长度为:")
for i in range(1,G.vexnum):
    print("%d - %d : %d"%(G.vexs[0], G.vexs[i], D[i]))
# '''