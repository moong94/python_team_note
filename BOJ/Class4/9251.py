string_1 = input()
string_2 = input()

lcs = [[0] * (len(string_1) + 1) for _ in range(len(string_2) + 1)]

for i in range(len(string_1)):
    for j in range(len(string_2)):
        if string_1[i] == string_2[j]:
            lcs[j + 1][i + 1] = lcs[j][i] + 1
        else:
            lcs[j + 1][i + 1] = max(lcs[j + 1][i],lcs[j][i + 1])

print(lcs[-1][-1])