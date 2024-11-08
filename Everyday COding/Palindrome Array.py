def Solution(arr):
    count = 0
    for n in arr:
        if str(n) == str(n)[::-1]:
            count+=1
    if count == len(arr):
        return True
    else:
        return False


