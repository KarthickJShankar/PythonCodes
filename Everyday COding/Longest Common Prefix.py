def Solution(arr):

    if len(arr) == 1:
        return arr[0]
    min_val = min(arr)
    for n in range(len(min_val),0 , -1):
        count = 0
        for m in arr:
            if min_val[:n] == m[:n]:
                count += 1
        if count == len(arr):
            return min_val[:n]
    return -1


print(Solution(["zpnoagxhicrmwhbc","ixgvg", "fiaxfxa", "bznpakvwfwrtvt",
                "lxvaencnlgikdexiajda", "emlwukecloqblue" ,"qeffrutlia",
                "by" ,"ynmfqplizpwhpkyqlp" ,"yetcxqywolw", "kuxel",
                "padgaokxdpbf", "ddsmxhaiuhvsgvhdwkbp"]))
