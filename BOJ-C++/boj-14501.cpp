#include <iostream>
using namespace std;
int N, T[16], P[16], dp[16];
int main() {
    cin >> N;
    for(int i = 1; i <= N; i++){
        cin >> T[i] >> P[i]; 
    } 
    for(int i = N; i >= 1; i--){
        if(i + T[i] - 1 > N){
            dp[i] = dp[i + 1];
            continue;
        }
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]]);
    }
    cout << dp[1]; 
    return 0;
}
