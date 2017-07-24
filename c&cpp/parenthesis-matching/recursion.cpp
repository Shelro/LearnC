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
	while (*s) //�����ַ���
	{
		if (*s == '(') //����������ƥ��
		{
			char *p = match(s + 1);
			if (p) //ƥ����ȷ
			{
				temp[i++] = ' ';
				while (s < p)
				{
					temp[i++] = ' ';
					s++;
				}
			}
			else { //δ��ƥ��
				temp[i++] = '$';
				err++;
			}
		}
		else if (*s == ')') //��Ϊƥ����ȷʱ��������)�����������������������˵��������
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