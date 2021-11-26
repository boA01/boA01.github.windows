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
'''

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