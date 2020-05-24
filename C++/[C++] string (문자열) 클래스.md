# [C++] string (문자열) 클래스

문자열 처리를 목적으로 정의된 라이브러리 클래스



<br>

<br>



## 특징

char * 형식의 C언어 문자열 처리 가능

string 클래스의 문자열 데이터는 char* 포인터 변수와 new를 이용하여 처리

산술연산, 비교연산 등 연산자 오버로딩 기능이 있어서 문자열 처리가 쉬움



<br>

<br>



## 헤더파일의 구분

* C언어 문자열 처리를 위한 헤더파일 #include <cstring>
* C++ 문자열 처리를 위한 헤더파일 #include <string> 
  * string.h (cstring의 구헤더명) 과 다르다



<br>

<br>



## 생성방법

* `string str1("hello");`
* `string str2 = "hello";`
* `string str3(str1);`



<br>

<br>



## 데이터 처리 함수

### 🍀 string 인자 접근관련 (access)

### str1.at(index) 

* `char& at (size_t index)`
* str1.at(0) -> 'h'

### str1.operator[index]

* `char& operator[size_t index]`
* str1.operator[0] -> 'h' == str1[0] -> 'h'

### str1.front()

* `char& front()`
* str1.front() -> 'h'

### str1.back()

* `char& back()`
* str1.back() -> 'o'



<br>



### 🍀 string size 관련

### str1.size()

* `size_t size() const` 사이즈 반환
* str1.size() -> 5

### str1.length()

* `size_t length() const` 길이 반환
* str1.length() -> 5

### str1.capacity()

* `size_t capacity() const` 할당된 메모리 크기(bytes) 반환.
* str1.capacity()

### str1.resize(n)

* `void resize(size_t n, char c). n만큼의 크기로 만듦. 

### str1.shrink_to_fit()

* `void shrink_to_fit()` 낭비되고 있는 capacity(메모리)를 줄임

### str1.reserve(n)

* `void reserve(size_t n = 0)` 파일 읽을 때 많이 사용. 미리 메모리를 할당해, capacity가 사이즈에 맞게 계속 늘어나는 행위를 덜하게해서 성능저하를 줄임. (성능저하 예시, 노래방2인실->4인실->8인실)

### str1.clear()

* `void clear()`

### str1.empty()

* `bool empty() const `  비었는지 확인. 
* 기준 : size, length가 0 (* capacity는 무관). 비었으면 true 리턴.



<br>



### 🍀 string 가지고 놀기

### str1.c_str()

* `const char* c_str() const`  string 마지막에 \0를 추가. c언어처럼 바뀜.

### str1.substr(....)

* `string substr(size_t index = 0, size_t len = npos) const`  index에서부터 len만큼 잘라서 반환

### str1.replace(....)

* `string& replace(size_t index, size_t len, const string& str)` 
* index 위치에서 len 길이까지의 범위를 매개변수로 들어온 str로 대체
* str1.replace(5, 2, str2)  / "Block**DM**ask" -> BlockBlogBlogBlogBlogask

### str1.compare(....)

* `int compare(const string& str2) const`
* `int compare(size_t index, size_t len, const string& str2) const`
* `int compare(size_t index, size_t len, const string& str2, size_t index2, size_t len2) const`

### str1.copy(....)

* `size_t copy(char* arr, size_t len, size_index = 0) const`

* ```
  char arr[10];
  int arrLen = str1.copy(arr, 3, 5);  //arrLen== 3, arr == 'Mas'
  arr[arrLen] = '\0';   //arr == 'Mas\0'
  ```

### str1.find(....)

* `size_t find (const string& str, size_t index = 0) const` 

* `size_t find (const char* arr, size_t index = 0) const`

* 일치하는 부분의 첫번째 순서(index) 반환

* ```
  str2.find("Blog")  // 0반환
  str2.find("Blog", 5) //8반환 BlogBlogBlogBlog 5번째가 'l'로 다르니 그 다음 Blog의 B index
  ```

### str1.push_back(c)

* `void push_back(char c)`
* 함수를 호출하는 string의 맨 뒤에 문자 c를 더함

### str1.pop_back()

* `void pop_back()`
* 함수를 호출하는 string의 맨 뒤에 문자 하나 없앰

### str.insert(pos, str2)

* pos 위치에 str 문자열 데이터 삽입 

### str.erase(pos, length)

* pos위치에서 length 길이 만큼 데이터 삭제



<br>



### 🍀 string iterator 종류

### str1.begin()

* `iterator begin()`
* 문자열의 첫 번째 문자 가리킴

### str1.end()

* `iterator end()`
* `const_iterator end() const`
* 문자열의 지막의 바로 다음 



<br>



### 🍀 string의 기타 

### swap(str1, str2)

* `void  swap (string& st1, string& str2)`
* str1과 str2 바꾸는 것. 복사 아닌 참조를 교환해 성능저하 X

### str1 데이터와 str2 데이터를 문자 비교 (true / false)

== 	!=	<	>	<=	>=



<br>

<br>



## string 예제 1

```
#include <iostream>
#include <string>
using namespace std;

int main(){
	string temp;
	cout << "여백 없는 문자열 입력 : ";
	cin >> temp;
	cout << "여백 없는 문자열 입력 결과  : " << temp << endl;
	cin.ignore(); //입력 버퍼에서 개행 문자 삭제
	
	
	
	cout << "여백 있는 문자열 입력 : " ;
	getline(cin, temp);
	cout << "여백 있는 문자열 입력 결과 : " << temp << endl;
	
		
	return 0; 
}
```



<br>



## string 예제 2

```
#include <iostream>
#include <string>
using namespace std;

int main(void){
	string str1 = "BlockDMask";
	string str2 = "BlogBlogBlogBlog";
	
	
	//push_back, pop_back
	str1.push_back('4');
	cout << str1 << endl;
	//str1.pop_back();
	//cout << str1 << endl;
	
	// str2.resize(4);  //Blog 4 4 16
	//str2.shrink_to_fit(); //
	//str2.clear(); // 0 0 16
	int size = str2.size();
	int length = str2.length();
	int capacity = str2.capacity();
	cout << str2 << ' ' << size << ' ' << length << ' ' << capacity << endl;
	//BlogBlogBlogBlog 16 16 16
	
	//find
	cout << str1.find("DM") << endl;  //5
	cout << str2.find("Blog") << endl;  //0
	cout << str2.find("Blog", 5) << endl;  //8
	
	// operator[], atr
	cout << str1[0] << endl;  //B
	cout << str1.at(0) << endl;  //B
	
	//front, back
	//cout << str1.front() << endl;  //B
	//cout << str1.back() << endl;  //k
	
	//iterator begin(), end() // B l o c k D M a s k 4
	string::iterator iter = str1.begin();
	for(; iter != str1.end(); ++iter){
		cout << *iter << ' ';
	} 
	cout << endl;
	
	
	system("pause");
	return 0;
}
```



참고

- 정혜경 c++
- https://blockdmask.tistory.com/338