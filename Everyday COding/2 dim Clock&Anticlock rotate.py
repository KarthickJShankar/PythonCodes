import numpy
def Solution(arr):
    final_arr_clockwise = []
    final_arr_anti_clockwise = []
    #clockwise
    for n in range(len(arr)):
        new_arr_clock = []
        for m in range(len(arr[0])-1,-1,-1):
            new_arr_clock.append(arr[m][n])
        final_arr_clockwise.append(new_arr_clock)
    #Anti-CLockwise
    for n in range(len(arr)-1,-1,-1):
        new_arr_anti_clock = []
        for m in range(len(arr[0])):
            new_arr_anti_clock.append(arr[m][n])
        final_arr_anti_clockwise.append(new_arr_anti_clock)

    print(numpy.array(final_arr_clockwise))
    print((numpy.array(final_arr_anti_clockwise)))





a = [
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35]
]
Solution(a)