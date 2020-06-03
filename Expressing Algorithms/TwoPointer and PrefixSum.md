# 배열의 특정 연속된 구간을 처리하는 경우

* 연속된 데이터 구간을 처리하기 원한다면?

* 가장 먼저, 투 포인터와 구간합 생각해보기



## 투 포인터 (Two pointers)

![image](https://user-images.githubusercontent.com/49062985/83651525-87f7f900-a5f4-11ea-8a7b-e98df6c91fa8.png)

### 투 포인터 문제 해결 방법 

#### 투 포인터란?

리스트에 순차적으로 접근해야할 때 두 개의 점을 이용해 위치를 기록하며 처리하는 기법

#### 알고리즘 설명

1. 시작점 (start)와 끝점(end)이 첫 번째 원소의 인덱스 (0)를 가리키도록 한다.
2. 현재 부분 합이 M과 같다면, 카운트 한다.
3. 현재 부분 합이 M보다 작거나 같다면, end를 1 증가시킨다.
4. 현재 부분 합이 M보다 크다면, start를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.



>  c++ 코드

```
#include <iostream>
using namespace std;
int main() {
	// n:데이터의 개수, m:부분연속 수열의 합
	int n = 5, m = 5;
	int result = 0, sum = 0, end = 0;
	int data[] = { 1, 2, 3, 2, 5 };
	for (int start = 0; start < n; start++) {
		while (sum < m && end < n) {
			sum += data[end];
			end += 1;
		}
		if (sum == m)
			result += 1;
		sum -= data[start];
	}
	cout << result;
	return 0;
}
```

> python 코드

```
n, m = 5, 5
data = [1,2,3,2,5]
result = 0
summary = 0
end = 0
for start in range(n):
    while summary < m and end < n:
        summary += data[end]
        end +=1
    if summary == m:
        result +=1
    summary -= data[start]
print(result)
```



<br>

<br>







## 구간 합 (Interval sum)

![image](https://user-images.githubusercontent.com/49062985/83651578-9ba35f80-a5f4-11ea-8c83-45d4ea4840cb.png)

### 문제 해결 방법

#### prefix sum 이란?

접두사 합이다.

#### 알고리즘 설명

1. Prefix Sum을 계산하여 배열 prefix_sum에 저장
2. 매 M개의 쿼리 정보를 확인할 때, 구간 합은 prefix_sum[ right ] - prefix_sum[ left - 1 ]

![image](https://user-images.githubusercontent.com/49062985/83651369-6139c280-a5f4-11ea-8ce4-7664b4b12ad5.png)





> c++ 코드

```
#include <iostream>
using namespace std;
int main() {
	int n, sum = 0, left, right;
	int data[1000], prefix_sum[1000] = {};
	// 데이터 개수 N입력
	cin >> n;
	
	// 데이터 입력 받기
	for (int i = 0; i < n; i++) {
		cin >> data[i];
	}

	// 구간 입력
	cin >> left >> right;

	// prefix_sum 배열 계산
	for (int i = 0; i < n; i++) {
		sum += data[i];
		prefix_sum[i + 1] = sum;
	}

	// 구간 합 계산
	cout << prefix_sum[right] - prefix_sum[left - 1];
	return 0;
}
```



> python 코드

```
n = 5
data = [10, 20, 30, 40, 50]

summary = 0
prefix_sum = [0]
for i in data :
    summary += i;
    prefix_sum.append(summary)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
```

