def Solution(sen):
    x = sen.split()
    return ' '.join(x[::-1])



s = "i like this program very much"
print(Solution(s))