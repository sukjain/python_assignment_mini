def rec(x):
    size = len(x)
    rep = []
    for l in range(size):
        for i in range(len(x[l])):
            k = i + 1
            for j in range(k, len(x[l])):
                if x[l][i] == x[l][j]:
                    rep.append(x[l][i])
                    break;
    for i in range(len((rep))):
        print(rep[i], rep.count(rep[i]) + 1)


x = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
rec(x)
