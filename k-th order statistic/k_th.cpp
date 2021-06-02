//
// Created by kolaq on 27.05.2021.
//

#include <iostream>
#include <vector>
//#include <algorithm>

std::vector<int> create_array(int p, int n, int q, int v) {
    std::vector<int> arr;
    arr.push_back(p);

    for (int i = 1; i < n; i++) {
        arr.push_back((arr[i - 1] * q) % v);
    }

    return arr;
}

int partition(int* &arr, int begin, int end) {
    int piv_idx;

    std::swap(arr[end - 1], arr[(begin + end - 1) / 2]);
//    std::iter_swap(arr.begin() + end - 1, arr.begin() + (begin + end - 1) / 2);
    piv_idx = begin;

    for (int j = begin; j < end; j++) {
        if (arr[j] < arr[end - 1]) {
            std::swap(arr[piv_idx], arr[j]);
//            std::iter_swap(arr.begin() + piv_idx, arr.begin() + j);
            piv_idx++;
        }
    }

    std::swap(arr[end - 1], arr[piv_idx]);
//    std::iter_swap(arr.begin() + end - 1, arr.begin() + piv_idx);

    return piv_idx;
}

void k_th(int* &arr, int k, int n) {
    int begin = 0, end = n, pivot;

    while (true) {
        if (end - begin <= 1)
            return;

        pivot = partition(arr, begin, end);

        if (pivot == k)
            return;
        else if (k < pivot)
            end = pivot;
        else
            begin = pivot + 1;
    }
}

//void print(std::vector<int> const &input) {
//    for (int i = 0; i < input.size(); i++) {
//        std::cout << input.at(i) << ' ';
//    }
//    std::cout << '\n';
//}
//
//void printArray(int arr[], int size)
//{
//    int i;
//    for (i=0; i < size; i++)
//        printf("%d ", arr[i]);
//    printf("\n");
//}

int main() {
//    int Q = 343, V = 32767, P = 3, N = 10, K = 7;
    int Q, V, P, N, K;
    std::cin >> Q >> V >> P >> N >> K;

    std::vector<int> nums = create_array(P, N, Q, V);
    int* numa = &nums[0];

//    printArray(numa, N);
//    print(nums);

    k_th(numa, K, N);
//    print(nums);

    std::cout << numa[K - 1];
    return 0;
}