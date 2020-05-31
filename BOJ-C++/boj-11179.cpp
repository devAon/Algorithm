#include <iostream>
#include <stack>
using namespace std;
stack<int> s;
void tenToTwo(int x) {
	if (x == 0) return;
	else {
		s.push(x % 2);
		tenToTwo(x / 2);
	}
}
int main() {
	int N, result = 0, data = 1;
	cin >> N;
	tenToTwo(N);
	while (!s.empty()) {
		result += s.top() * data;
		data = data * 2;
		s.pop();
	}
	cout << result;
	return 0;
}
