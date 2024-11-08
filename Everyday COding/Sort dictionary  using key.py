
def Solution(arr,k):
    return sorted(arr,key=lambda x:x[k])


data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print(Solution(data,"age"))