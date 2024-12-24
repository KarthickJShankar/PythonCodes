def solution(st):
    roman_dict = {'X' : 10, 'I' : 1, 'V' : 5}
    present_value = 0
    result = 0
    for n in st[::-1]:
        current_val = roman_dict[n]
        if current_val<present_value:
            result -= current_val
        else:
            result += current_val
        present_value = current_val
    return result

print(solution('XI'))