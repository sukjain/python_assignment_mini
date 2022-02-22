dict_1 = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

print("The original dictionary is : " + str(dict_1))

res = []
for key, val in dict_1.items():
    res.append([key] + val)

print("The converted list is : " + str(res))

