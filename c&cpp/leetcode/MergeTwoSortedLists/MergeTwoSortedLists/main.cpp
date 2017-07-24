#include <iostream>
#include <array>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (l1 == NULL && l2 == NULL) {
			return NULL;
		}
		if (l1 == NULL) {
			return l2;
		}
		else if(l2 ==NULL) {
			return l1;
		}
		ListNode* current = NULL;
		ListNode* first = NULL;
		if (l1->val <= l2->val) {
			current = new ListNode(l1->val);
			l1 = l1->next;
		}
		else {
			current = new ListNode(l2->val);
			l2 = l2->next;
		}
		first = current;
		while (l1!=NULL && l2!=NULL){
			ListNode* newElement;
			if (l1->val <= l2->val) {
				newElement = new ListNode(l1->val);
				current->next = newElement;
				current = current->next;
				l1 = l1->next;
			}
			else {
				newElement = new ListNode(l2->val);
				current->next = newElement;
				current = current->next;
				l2 = l2->next;
			}
		}
		if (l1 == NULL) {
			current->next = l2;
		}
		else{
			current->next = l1;
		}
		return first;
	}

	void print(ListNode* l) {
		if (l == NULL) cout << "NULL";
		while (l != NULL) {
			cout << l->val<<endl;
			l = l->next;
		}
	}
};

int main() {
	ListNode *l1;
	ListNode *l2;
	array<int, 8> a1 = { -3,5,9,10,23,56,89,100 };
	array<int, 2> a2 = { 4,5 };
	ListNode* next1 = NULL;
	ListNode* next2 = NULL;
	next1 = &ListNode(a1[0]);
	next2 = &ListNode(a2[0]);
	l1 = next1;
	l2 = next2;
	for (int i = 1; i < a1.size(); i++) {
		ListNode* current = new ListNode(a1[i]);
		next1->next = current;
		next1 = next1->next;
	}
	for (int i = 1; i < a2.size(); i++) {
		ListNode* current = new ListNode(a2[i]);
		next2->next = current;
		next2 = next2->next;
	}
	Solution s;
	ListNode* result;
	result = s.mergeTwoLists(l1, l2);
	s.print(result);

	return 0;
}