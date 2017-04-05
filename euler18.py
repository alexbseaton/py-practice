rows = []
with open('p067_triangle.txt', 'r') as triangle:
    for row in triangle:
        rows.append(list(map(int, row.split())))

# dict with keys (row, column) and values the highest sum possible of paths to that position
max_sum = {(0, 0) : rows[0][0]}
def max_sum_at_parent(row, column, max_sum_dict):
    if column == 0:
        return max_sum_dict[(row - 1, column)]
    elif column == len(rows[row]) - 1:
        return max_sum_dict[(row - 1, column - 1)]
    else:
        return max(max_sum_dict[(row - 1, column - 1)], max_sum_dict[(row - 1, column)])
# populate the dictionary
for row in range(1, len(rows)):
    for column in range(len(rows[row])):
        max_sum[(row, column)] = max_sum_at_parent(row, column, max_sum) + rows[row][column]
# find the maximum value held in the bottom row of the dictionary
print(max([max_sum[len(rows) - 1, column] for column in range(len(rows))]))
