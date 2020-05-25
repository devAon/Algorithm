#include <iostream>
using namespace std;
int main(){
	int N, Y = 0, M = 0, value;
	cin >> N;
	for(int i = 0; i < N; i++) {
		cin >> value;
		Y += (value / 30 + 1) * 10;
		M += (value / 60 + 1) * 15;
	}
	if(Y < M)
		cout << "Y " << Y; 
	else if(M < Y)
		cout << "M " << M; 
	else
		cout << "Y M " << Y;
}
