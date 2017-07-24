//
//  main.cpp
//  3Sum
//
//  Created by Shelro on 2017/6/28.
//  Copyright © 2017年 Yiyi Chang. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
	/*
    vector<vector<int>> threeSum(vector<int>& nums) {
        int sum = 0;
		int lasti = 0, lastj = 0;
        vector<vector<int>> result;
		std::sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 2; i++){
			if (nums[i] == lasti) {
				continue;
			}
            for(int j = i + 1; j < nums.size() - 1; j++){
                sum = nums[i] + nums[j];
				if (sum > 0) {
					break;
				}
				if (sum + nums[nums.size() - 1] < 0 || lastj == nums[j]) {
					continue;
				}
                for(int t = j + 1; t < nums.size(); t++){
                    if(sum + nums[t]==0){
                        vector<int> element;
						element = { nums[i], nums[j], nums[t] };
						lasti = nums[i];
						lastj = nums[j];
						result.push_back(element);
						break;
                    }
                }
            }
        }
        return result;
    }*/

	
	vector<vector<int> > threeSum(vector<int> &num) {
		vector<vector<int> > res;
		std::sort(num.begin(), num.end());
		for (int i = 0; i < num.size(); i++) {
			int target = -num[i];
			int front = i + 1;
			int back = num.size() - 1;
			while (front < back) {
				int sum = num[front] + num[back];
				
				// Finding answer which start from number num[i]
				if (sum < target)
					front++;
				
				else if (sum > target)
					back--;
				else {
					vector<int> triplet(3, 0);
					triplet[0] = num[i];
					triplet[1] = num[front];
					triplet[2] = num[back];
					res.push_back(triplet);
					// Processing duplicates of Number 2
					// Rolling the front pointer to the next different number forwards
					while (front < back && num[front] == triplet[1]) front++;
					// Processing duplicates of Number 3
					// Rolling the back pointer to the next different number backwards
					while (front < back && num[back] == triplet[2]) back--;
				}
			}
			
			// Processing duplicates of Number 1
			while (i + 1 < num.size() && num[i + 1] == num[i])
				i++;
		}
		return res;
	}
};

int main(int argc, const char * argv[]) {
    vector<int> num;
    num = { -1,0,1,2,-1,-4,20,-6,5,8,3,9,10,30,8,8,8,-6,13 };
    vector<vector<int>> result;
    Solution s;
    result = s.threeSum(num);
    for(int i = 0;i<result.size();i++){
        for(int j=0;j<3;j++){
            cout << result[i][j] << "," ;
        }
        cout << endl;
    }
}
