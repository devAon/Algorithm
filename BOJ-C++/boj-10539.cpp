#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	int n, sum = 0;
	cin >> n;
	vector<int> A(n), B(n);
	for (int i = 0; i < n; i++) {
		cin >> B[i];
	}
	A[0] = B[0];
	sum += A[0];
	for (int i = 1; i < n; i++) {
		A[i] = (i + 1) * B[i] - sum;
		sum += A[i];
	}
	for (int i = 0; i < n; i++) {
		cout << A[i] << ' ' ;
	}
	return 0;
}