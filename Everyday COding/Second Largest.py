arr = [10, 20, 4, 450, 99, 450]
def Solution(arr):
    # temp = arr[0]
    # for n in arr:
    #     if n!=max(arr):
    #         if temp < n:
    #             temp = n
    # return temp
    if len(arr)<2:
        return None
    largest = second_largest = float('-inf')
    for n in arr:
        if n > largest:
            second_largest = largest
            largest=n
        elif n > second_largest and n!=largest:
            second_largest = n
    return second_largest

print(Solution(arr))