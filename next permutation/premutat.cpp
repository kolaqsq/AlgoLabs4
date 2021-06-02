//
// Created by kolaq on 02.06.2021.
//

#include <iostream>
#include <vector>

using namespace std;

void nextPermutation(vector<int> &nums) {
    int len = nums.size();
    int i = len - 2;

//        finding first a[i] < a[i + 1]
    for (; i >= 0 && nums[i] >= nums[i + 1]; i--);

//    making part after a[i] accenting
    int j = i + 1;
    int k = len - 1;
    while (j < k) {
        swap(nums[j], nums[k]);
        j++;
        k--;
    }

//    exit point if input array was descending
    if (i == -1)
        return;

//    swap a[i] with a just larger number to make permutation legit
    for (j = i + 1; j < len; ++j) {
        if (nums[j] > nums[i]) {
            swap(nums[i], nums[j]);
            break;
        }
    }
}

int main() {
    vector<int> numa = {1, 5, 8, 4, 7, 6, 5, 3, 1};
    nextPermutation(numa);

    return 0;
}