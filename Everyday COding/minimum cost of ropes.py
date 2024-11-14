def solution(arr):
    x = sorted(arr)

    sum_x = x[0]
    new_list = []
    for n in range(1,len(x)):
        sum_x +=x[n]
        new_list.append(sum_x)
    return sum(new_list)


print(solution([2,8,22,75,27,22,5,12]))
