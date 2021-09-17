'''
#include <iostream>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define INF 0x3f3f3f3f
using namespace std;
 
int dp[1 << 20], sum[1 << 20];
 
int main(int argc, char* argv[]){
 
    using pair_t = pair<int, int>;
    int n;
    cin >> n;
    vector<pair_t> works(n);
    const int maxn = (1 << n);
    memset(dp, INF, sizeof(dp));
    dp[0] = 0;
    for(int i = 0; i < n; i++) cin >> works[i].first >> works[i].second;
    for(int i = 0; i < maxn; i++){
        for(int j = 0; j < n; j++){
            if(!(i & (1 << j))) {
                int u = i | (1 << j);
                sum[u] = sum[i] + works[j].second;
                dp[u] = min(dp[u], dp[i] + max(0, sum[u] - works[j].first));
            }
        }
    }
    cout << dp[maxn-1] << endl;
    return 0;
}
'''