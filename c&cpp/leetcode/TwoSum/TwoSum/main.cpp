//
//  main.cpp
//  TwoSum
//
//  Created by 张映艺 on 2017/6/3.
//  Copyright © 2017年 Yiyi Chang. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(int i = 0; i<nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]+nums[j] == target){
                    int t = 0;
                    for(;t<result.size();t++){
                        if(i==result[t]||j==result[t]){
                            break;
                        }
                    }
                    if(t==result.size()){
                        result.push_back(i);
                        result.push_back(j);
                    }
                }
            }
        }
        return result;
    }
};

int main(){
    vector<int> num;
    vector<int> r;
    char c;
    int n,t;
    cin >> c;
    while(c == '[' || c==','){
        cin >> n;
        cin >> c;
        num.push_back(n);
    }
    cin >>t;
    
    //r = Solution::twoSum(num, t);
    
    return 0;
}
