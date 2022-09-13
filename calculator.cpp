#include <iostream>
using namespace std;

int main(){
	int a,c;
	char b;
	cin>>a>>b>>c;
	switch (b){
	case '+':
		cout<<a+c;break;
	case '-':
		cout<<a-c;break;
	case '*':
		cout<<a*c;break;
	case '/':
		cout<<a/c;break;
	}return 0;
}
