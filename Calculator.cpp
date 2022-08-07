#include <stdio.h>
#include <ctype.h>
int main()
{

	char symbol;
	printf("\n");
	printf("[+]  [-]  [/] [*]\n");
	scanf("%s", &symbol);
	int a,b;
	scanf("%d %d",&a,&b);
	switch (symbol) {
	case '+' :
		printf("%d",a+b);
		break;
	case '-' :
		printf("%d",a-b);
		break;
	case '/' :
		printf("%d",a/b);
		break;
	case '*':
		printf("%d",a*b);
	default :
	printf("");
}

  return 0;
}
