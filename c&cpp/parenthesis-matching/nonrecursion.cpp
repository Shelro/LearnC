#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() 
{
	stack<char> s;
	vector<int> left;
	vector<int> right;
	vector<char> out;
	char v[100];
	int i = 0;
	cin.getline(v, 100);
	for (; i < 100; i++) {
		if (v[i] == '\0') break;
		if (v[i] != ')') {
			s.push(v[i]);
			if (v[i] == '(')
				left.push_back(i);
		}
		else {
			if (s.empty()) right.push_back(i);
			else {
				while (s.top() != '(') {
					s.pop();
					if (s.empty()) {
						right.push_back(i);
						break;
					}
				}
				if (!s.empty()) {
					s.pop();
					left.pop_back();
				}
			}
		}
	}
	for (int j = 0; j < i; j++) out.push_back(' ');
	if(left.size() != 0 && right.size() != 0){
		for (int k = 0; k < right.size(); k++) {
			out[right[k]] = '?';
		}
		for (int k = 0; k < left.size(); k++) {
			out[left[k]] = '$';
		}
	}
	else if (left.size() == 0) {
		for (int k = 0; k < right.size(); k++) {
			out[right[k]] = '?';
		}
	}
	else if (right.size() == 0) {
		for (int k = 0; k < left.size(); k++) {
			out[left[k]] = '$';
		}
	}
	
	if (left.size() == 0 && right.size() == 0) cout << "Amazing!\n";
	else {
		for (int j = 0; j < i; j++) {
			cout << out[j];
		}
		cout << endl;
	}
}