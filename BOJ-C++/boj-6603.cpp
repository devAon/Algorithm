#include<iostream>
#include<vector>
using namespace std;
int n;
int tmp[14];
void dfs(int index);
vector<int> lotto;
int main(void){
    while (true) {
        cin >> n;
        if (n == 0) return 0;
        else{
            for (int i = 0; i < n; i++)
                cin >> tmp[i];
            dfs(0);
            cout << endl;
        }
    }
}
void dfs(int index){
    if (lotto.size() == 6){
        for (int i = 0; i < 6; i++)
	        cout << lotto[i] << ' ';
        cout << endl;
        return;
    }else{
        for (int i = index; i < n; i++){
            lotto.push_back(tmp[i]);
            dfs(i + 1);
            lotto.pop_back();
        }
    }
}
