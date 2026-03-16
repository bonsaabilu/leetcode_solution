#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, 0, result);
        return result;
    }

private:
    void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
        if (start == nums.size()) {
            result.push_back(nums); // store one valid permutation
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);           // choose
            backtrack(nums, start + 1, result);   // explore
            swap(nums[start], nums[i]);           // un-choose (backtrack)
        }
    }
};
