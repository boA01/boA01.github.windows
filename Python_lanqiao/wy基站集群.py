'''
给你一个一维数组a，长度为n，表示了n个基站的位置高度信息。
数组的第i个元素a[i]表示第i个基站的海拔高度是a[i],而下标
相邻的基站才相邻并且建立链接，即x号基站与x-1号基站、x+1
号基站相邻。特别的，1号基站仅与2号相邻，而n号基站仅与n-1
号基站相邻。当一场海拔高度为y的洪水到来时，海拔高度小于等
于y的基站都会被认为需要停止发电，同时断开与相邻基站的链接。
'''
enb = int(input())
a_alti = [int(i) for i in input().split(" ")]
hx_t = int(input())
hx_h = [int(i) for i in input().split(" ")]
rsp_a = list(range(0, enb + 2))
rsp_a[0] = -1
rsp_a[enb + 1] = -1
hx_new_index = [index for index, value in sorted(enumerate(hx_h), key=lambda h: h[1])]
a_new_index = [index for index, value in sorted(enumerate(a_alti), key=lambda h: h[1])]
cluster_num = [0] * hx_t
k = 1
for i in range(hx_t):
    new_cluster = 0
    while k <= enb and a_alti[a_new_index[k-1]] <= hx_h[hx_new_index[i]]:
        if rsp_a[a_new_index[k-1]] == -1 and rsp_a[a_new_index[k-1]+2] == -1:
            new_cluster = new_cluster - 1
        elif rsp_a[a_new_index[k-1]] != -1 and rsp_a[a_new_index[k-1]+2] != -1:
            new_cluster = new_cluster + 1
        rsp_a[a_new_index[k-1]+1] = -1
        k = k + 1
    if i == 0:
        cluster_num[hx_new_index[i]] = 1 + new_cluster
    else:
        cluster_num[hx_new_index[i]] = cluster_num[hx_new_index[i - 1]] + new_cluster
for cn in cluster_num:
    print(cn)