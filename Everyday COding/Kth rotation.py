def solution(arr):
    x = sorted(arr)

    max_index = x.index(min(x))

    max_index_arr = arr.index(min(arr))

    return max_index_arr-max_index
print(solution([39,6,11,14,18,36,37,38]))