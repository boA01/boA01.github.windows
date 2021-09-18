'''
#include <iostream>
#include <iomanip>
using namespace std;
 
int main()
{
    int n;
    cin >> n;
     
    int target[10] = {1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870};
    double result[10] = {1.000000, 0.500000, 0.333333, 0.266667, 0.228571, 0.207792, 0.191808, 0.180525, 0.171024, 0.163588};
     
    int i = 0;
    if (n >= target[9])
        cout << "0.163588" << endl;
    else
    {
        while (n >= target[i])
            i++;
        cout << setiosflags(ios::fixed) << fixed << setprecision(6) << result[i - 1] << endl;
    }
     
    return 0;
}
'''