#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
	bool isValid(string s) {
		stack<char> slist;
		char c;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '}' || s[i] == ']' || s[i] == ')') {
				if (slist.empty()) {
					return false;
				}
				else {
					c = slist.top();
					if (c != '{'&&c != '['&&c != '(') {
						return false;
					}
					if (s[i] == '}') {
						if (c != '{') {
							return false;
						}
						slist.pop();
					}
					else if (s[i] == ']') {
						if (c != '[') {
							return false;
						}
						slist.pop();
					}
					else {
						if (c != '(') {
							return false;
						}
						slist.pop();
					}
				}
			}
			else {
				slist.push(s[i]);
			}
		}

		while (!slist.empty()) {
			return false;
		}

		return true;
	}
};

int main() {
	string s;
	cin >> s;
	Solution s1;
	cout << s1.isValid(s);
	return 0;
}