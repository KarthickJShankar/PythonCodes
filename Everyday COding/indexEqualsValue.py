def Soluton(arr):
    for n in range(len(arr)):
        if n+1 == arr[n]:
            print(arr[n],end=' ')

Soluton([1,2,3,3,4])