#include <iostream>
using namespace std;
int main(){
	int a[6], b[6], k, sum =0, max = 0, n;
	cin >> k;
	for(int i =0; i < 6; i++)
		cin >> a[i] >> b[i];
	for(int i = 0; i < 6; i++){
		if(max < b[i] * b[(i+1) % 6]){
			max = b[i]*b[(i+1)%6];
			n = i;
		}
	}
	sum = b[(n+3)%6]*b[(n+4)%6];
	max = max-sum;
	cout << max*k;
}
