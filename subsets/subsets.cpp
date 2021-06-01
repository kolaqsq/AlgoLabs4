//
// Created by kolaq on 01.06.2021.
//
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<vector<int>> subsets(vector<int> &nums) {
    int n = nums.size();
    int nth_bit = 1 << n;
    int bitmask = 0b0;
    vector<vector<int>> output = {{}};

    for (int i = 0; i < pow(2, n); ++i) {
        bitmask = bin()
    }

    return output;
}

int main() {
//    cout << (2 ^ 4);
}