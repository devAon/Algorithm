#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int arr[9], sum = 0, v1, v2;
	for (int i = 0; i < 9; i++) {
		cin >> arr[i];
		sum += arr[i];
	}
	sort(arr, arr + 9);
	for (int i = 0; i < 8; i++) {
		for (int j = i+1; j < 9; j++) {
			if (sum - (arr[i] + arr[j]) == 100) {
				v1 = i, v2 = j;
				break;
			}
		}
	}
	for (int i = 0; i < 9; i++) {
		if(i != v1 && i != v2)
			cout << arr[i] << endl;
	}
	return 0;
}
