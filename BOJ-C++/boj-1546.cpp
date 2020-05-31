#include <iostream>
using namespace std;
int main() {
	int N, score = 0, sum = 0, max = 0;
	cin >> N;
	for(int i =0; i < N; i++){
		cin >> score;
		sum += score;
		if(max < score) max = score;
	}
	cout << (float)sum / max * 100.000 / N;
	return 0;
}
