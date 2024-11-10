import numpy as np
# final_list = []
# for n in range(8):
#     for m in range(8):
#         if n%2 == 0:
#             a = np.zeros(8,int)
#             a[::2] = 1
#         else:
#             a = np.ones(8,int)
#             a[::2] = 0
#     final_list.extend(a)
# final_list = np.array(final_list).reshape(8,8)
# print(final_list)

a = np.zeros((8,8),int)
a[::2,::2] = 1
a[1::2, 1::2] = 1
print(a)