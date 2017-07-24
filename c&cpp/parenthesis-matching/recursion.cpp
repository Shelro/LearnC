#include <iostream>
using namespace std;
char * match(char *s)
{
	while (*s)
	{
		if (*s == '(')
		{
			char *p = match(s + 1);
			if (p) s = p;
			else
				break;
		}
		else if (*s == ')')
		{
			return s;
		}
		s++;
	}
	return NULL;
}
void match_brace(char *s)
{
	char temp[101], *ss = s;
	int i = 0, err = 0;
	while (*s) //遍历字符串
	{
		if (*s == '(') //遇到（进行匹配
		{
			char *p = match(s + 1);
			if (p) //匹配正确
			{
				temp[i++] = ' ';
				while (s < p)
				{
					temp[i++] = ' ';
					s++;
				}
			}
			else { //未能匹配
				temp[i++] = '$';
				err++;
			}
		}
		else if (*s == ')') //因为匹配正确时，会跳过)，所以这里如果遇到），则说明有问题
		{
			temp[i++] = '?';
			err++;
		}
		else
			temp[i++] = ' ';
		s++;
	}
	temp[i] = '\0';
	if (err)
	{
		cout << ss << endl;
		cout << temp << endl;
	}
}

int main()
{
	char str[101];
	while (cin.getline(str, sizeof(str)))
	{
		match_brace(str);
	}
	return 0;
}