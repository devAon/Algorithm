#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int arr[21], n = 10, a, b;
	for(int i = 1; i <= 20; i++) arr[i] = i;
	while(n--){
		cin >> a >> b;
		reverse(arr + a, arr + b +1);
	}
	for(int i = 1; i < 21; i++)
		cout << arr[i] << ' ';
}

