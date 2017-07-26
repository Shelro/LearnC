//
//  main.cpp
//  String to Integer
//
//  Created by Shelro on 2017/6/3.
//  Copyright © 2017年 Yiyi Chang. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        long long result = 0;
        bool isSub = false;
        bool isBlank = true;
        if(str==""){
            result = 0;
        }
        else{
            for(int i=0;i<str.size();i++){
                if(str[i]<48 || str[i]>57){
                    if(isBlank){
                        if(str[i]==43){
                            isBlank = false;
                            i++;
                            if(str[i]<48 || str[i]>57){
                                break;
                            }
                            else{
                                result=result*10+ str[i] - 48;
                            }
                        }
                        else if(str[i]==45){
                            isBlank = false;
                            isSub = true;
                            i++;
                            if(str[i]<48 || str[i]>57){
                                break;
                            }
                            else{
                                result=(-1)*(str[i]-48);
                            }
                        }
                        else if(str[i]==32){
                            continue;
                        }
                        else{
                            break;
                        }
                    }
                    else{
                        break;
                    }
                }
                else{
                    isBlank = false;
                    if(isSub){
                        result = result*10 - (str[i] - 48);
                    }
                    else{
                        result = result*10 + str[i] - 48;
                    }
                }
            }
        }
        isSub = false;
        return (int)result;
    }
};

int main(int argc, const char * argv[]) {
    string s;
    int a;
    s = "-2147483649";
    Solution s1;
    a = s1.myAtoi(s);
    
    int b = 214748364;
    b = b*10+8;
    cout << a<<endl<<INT_MIN<<endl<<b<<endl;
    return 0;
}

