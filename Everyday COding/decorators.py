def decorator(func):
    def wrapper(*arg):
        val = func(*arg)
        return val**3
    return wrapper

@decorator
def calculate(*args):
    temp = 1
    for n in args:
        temp *= n
    return temp

print(calculate(1,2,3))