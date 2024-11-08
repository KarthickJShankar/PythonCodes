def Solution(arr1,arr2):
    for n in arr1:
        if n in arr2:
            arr2.remove(n)
        else:
            return False
    if len(arr2)==0:
        return True

