#include <iostream>
#include <string>
using namespace std;
int tenToTow(int);
int twoToten(int);
int main(){
	int N;
	cin >> N;
	cout << twoToten(tenToTow(N));
}
int tenToTow(int num){
	int result = 0;
	for(int i = 1; num > 0; i *= 10){
		int binary = num % 2;
		result += binary * i;
		num /= 2;
	}
	return result;
}
int twoToten(int n){
	string s = to_string(n);
	reverse(s.begin(), s.end());
	int num = atoi(s.c_str());
	int result = 0, mul = 1;
	while(num > 0){
		if(num % 2) result += mul;
		mul *= 2;
		num /= 10;
	}
	return result;
}
