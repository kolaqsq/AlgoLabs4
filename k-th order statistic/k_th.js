function createArray(p, n, q, v) {
    let arr = [p];
    for (let i = 1; i < n; i++) {
        arr.push((arr[i - 1] * q) % v);
    }

    return arr;
}

function partition(arr, begin, end) {
    let pindex;

    [arr[end - 1], arr[~~((begin + end - 1) / 2)], pindex] =
        [arr[~~((begin + end - 1) / 2)], arr[end - 1], begin];

    for (let j = begin; j < end; j++) {
        if (arr[j] < arr[end - 1]) {
            [arr[pindex], arr[j], pindex] =
                [arr[j], arr[pindex], pindex + 1];
        }
    }

    [arr[end - 1], arr[pindex]] =
        [arr[pindex], arr[end - 1]];

    return pindex;
}

function k_th(arr, k) {
    let begin = 0, end = arr.length;

    while (true) {
        if (end - begin <= 1)
            return;

        let pivot = partition(arr, begin, end);

        switch (pivot) {
            case (pivot === k):
                return;

            case (k < pivot):
                end = pivot;
                break;

            default:
                begin = pivot + 1
                break;
        }
    }
}

let Q = 343, V = 32767, P = 3, N = 10, K = 7
let nums = createArray(P, N, Q, V)
console.log(nums)
k_th(nums, K)
console.log(nums, nums[K - 1])
