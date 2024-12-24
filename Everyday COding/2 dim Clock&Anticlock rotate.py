import numpy
# def Solution(arr):
#     final_arr_clockwise = []
#     final_arr_anti_clockwise = []
#     #clockwise
#     for n in range(len(arr)):
#         new_arr_clock = []
#         for m in range(len(arr[0])-1,-1,-1):
#             new_arr_clock.append(arr[m][n])
#         final_arr_clockwise.append(new_arr_clock)
#     #Anti-CLockwise
#     for n in range(len(arr)-1,-1,-1):
#         new_arr_anti_clock = []
#         for m in range(len(arr[0])):
#             new_arr_anti_clock.append(arr[m][n])
#         final_arr_anti_clockwise.append(new_arr_anti_clock)
#
#     print(numpy.array(final_arr_clockwise))
#     print((numpy.array(final_arr_anti_clockwise)))

def rotate_clockwise(matrix):
    # Transpose the matrix
    transposed = [list(row) for row in zip(*matrix)]
    print(transposed)
    # Reverse each row
    return [row[::-1] for row in transposed]

def rotate_anticlockwise(matrix):
    # Transpose the matrix
    transposed = [list(row) for row in zip(*matrix)]
    print(transposed)
    # Reverse the order of rows
    return transposed[::-1]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

clockwise = rotate_clockwise(matrix)
print("Clockwise rotation:")
# for row in clockwise:
#     print(row)

# Rotate 90 degrees anticlockwise
anticlockwise = rotate_anticlockwise(matrix)
print("\nAnticlockwise rotation:")
for row in anticlockwise:
    print(row)

# import numpy as np
#
#
# a = [
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25],
#     [26, 27, 28, 29, 30],
#     [31, 32, 33, 34, 35]
# ]
# a = np.array(a)
# # Solution(a)
# x = np.flip(a.T,axis=1)
# print(x)