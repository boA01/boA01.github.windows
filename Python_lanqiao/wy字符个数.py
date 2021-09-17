x = input()
n = int(input())

arr = list(map(lambda o:bin(int(o))[2:].count(x), input().split(' ')))
print(len(set(arr)))

'''
//位运算 + 去重

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int main(){
    int T;
    cin>>T;
    int n;
    int num;
    while(T--){
        cin>>n;
        unordered_map<int, int> mp;
        for(int i = 0; i < n; ++i){
            cin>>num;
            int count = 0;
            while(num){
                num = num & (num - 1);
                count++;
            }
            mp[count]++;
        }
        cout<<mp.size()<<endl;
    }
    return 0;
}
'''