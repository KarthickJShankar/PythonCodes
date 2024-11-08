def generator(arr):
    for n in arr:
        yield n


generate = generator([1,2,3,4,5,6])
for n in generate:
    print(n)