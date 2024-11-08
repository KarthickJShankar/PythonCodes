def leftRotate(arr, d):
    # code here
    new_arr = []
    for n in range(d, len(arr)):
        new_arr.append(arr[n])
    for n in range(d):
        new_arr.append(arr[n])
    return new_arr

print(leftRotate([1,2,3,4,5],2))