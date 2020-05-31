#include <iostream>
using namespace std;
int main(){
	int K, A[100]={}, B[100]={}, a = 0, b = 1;
	cin >> K;
	A[2] = 1, B[1] = 1, B[2] = 1;
	for(int i = 2; i <= K; i++){
		A[i] = B[i-1]; 
		a = A[i];
		B[i] = A[i-1] + B[i-1];
		b = B[i];
		if(i == 2){
			a = 1;b = 1;
		}	
	}
	cout << a << ' ' << b;	
}
