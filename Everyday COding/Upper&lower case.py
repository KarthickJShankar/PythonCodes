st = "Hello World"
def Solution(st):
    st = ''.join(st.split(' '))
    print(st)
    upper = 0
    lower = 0
    for n in st:
        if n.isupper():
            upper+=1
        elif n.islower():
            lower+=1
    return f"The Number of Uppercase is: {upper} " + "and" + f" The Number of LowerCase is :{lower}"

print(Solution(st))

