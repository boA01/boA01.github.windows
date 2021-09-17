n = int(input())
arr = map(int, input().split(" "))
d = []

for i in range(n):
    W = next(arr)
    H = next(arr)
    print(W,H)
    d.append({'k':f'{H} {W}','v':H*W})

for i in sorted(sorted(d,key=lambda x:x.get("v")),key=lambda y:y.get('k').split(' ')[0]): #按面积
    print(i.get("k"),end=' ')

'''
#define INF 1e-9
  
struct node {
    int w, h;
};
  
bool cmp(node a, node b) {
    if (a.w * a.h < b.w * b.h) return true;
    else if (a.w * a.h > b.w * b.h) return false;
    else {
        double wa = a.w, ha = a.h, wb = b.w, hb = b.h;
        double v1 = min(wa / ha, ha / wa);
        double v2 = min(wb / hb, hb / wb);
        if (v1 - v2 < -INF) return false;
        else if (v1 - v2 > INF) return true;
        else {
            if (a.w < b.w) return true;
            else return false;
        }
    }
}
  
int main() {
      
    int n;
    scanf("%d", &n);
    vector<node> res(n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &res[i].w, &res[i].h);
    }
    sort(res.begin(), res.end(), cmp);
    for (int i = 0; i < n; ++i) {
        i == n - 1 ? printf("%d %d\n", res[i].w, res[i].h) : printf("%d %d ", res[i].w, res[i].h);
    }
      
    return 0;
}
'''