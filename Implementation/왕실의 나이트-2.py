input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) +  1

steps = [(-2,-1), (-2,1), (2, -1), (2, 1), (-1,-2), (-1, 2), (1,-2), (1, 2)]

result = 0

for i in steps:
    next_row = row + i[1]
    next_column = column + i[0]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)