#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main() {
	int N, M, minLen;
	string A, B, AB;
	int alpa[26] = { 3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1 };
	cin >> N >> M >> A >> B;
	vector<int> v(N + M);
	minLen = min(N, M);
	for (int i = 0; i < minLen; i++) {
		AB += A[i];
		AB += B[i];
	}
	if (N > M) {
		for (unsigned int i = minLen; i < A.length(); i++)
			AB += A[i];
	}else if (N < M) {
		for (unsigned int i = minLen; i < B.length(); i++)
			AB += B[i];
	}
	for (int i = 0; i < N + M; i++)
		v[i] = alpa[AB[i] - 'A'];

	for (int i = 0; i < N + M - 2; i++) 
		for (int j = 0; j < N + M - i - 1; j++) 
			v[j] = (v[j] + v[j + 1])%10;

	if(v[0] % 10 == 0)
		cout << v[1] % 10 << '%';
	else
		cout << v[0] % 10 << v[1] % 10 << '%';
	return 0;
}