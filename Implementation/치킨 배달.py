from itertools import combinations

n, m = map(int, input().split())

city = []
for _ in range(n):
    r = list(map(int, input().split()))
    city.append(r)

house = []
store = []

for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            house.append((x,y))
        elif city[x][y] == 2:
            store.append((x,y))

remain = list(combinations(store,m))

answer_case = []

for case in remain:
    chicken_case = []
    for i in house:
        house_loc = []
        for j in case:
            house_loc.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
        chicken_case.append(min(house_loc))
    answer_case.append(sum(chicken_case))

answer = min(answer_case)
print(answer)
