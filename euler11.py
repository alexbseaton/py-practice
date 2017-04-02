from functools import reduce
from operator import mul

rows = []
with  open("grid.txt", "r") as file:
    for line in file:
        line = line.strip('\n')
        entries = []
        for entry in line.split(' '):
            entries.append(int(entry))
        rows.append(entries)

height = len(rows)
for row in rows:
    assert len(row) == height

def product_of(arr):
    assert len(arr) == 4
    return reduce(mul, arr)

# across
def greatest_product_across(rows):
    greatest_product = 0
    height = len(rows)
    for row in rows:
        for start in range(height - 3):
            if product_of(row[start:start + 4]) > greatest_product:
                greatest_product = product_of(row[start:start + 4])
    return greatest_product

candidates = [greatest_product_across(rows)]
# down
columns = []
for i in range(height):
    new_column = []
    for j in range(height):
        new_column.append(rows[j][i])
    columns.append(new_column)

down = greatest_product_across(columns)
candidates.append(down)

# diagonal
def greatest_product_diag(rows):
    result = 0
    for start_row in range(height - 3):
        for start_col in range(height - 3):
            to_multiply = []
            for i in range(4):
                to_multiply.append(rows[start_row + i][start_col + i])
            if product_of(to_multiply) > result:
                result = product_of(to_multiply)
    return result

#assert greatest_product_diag(rows) == 11 ** 4
candidates.append(greatest_product_diag(rows))

left_diags = 0
for start_row in range(3, height):
    for start_col in range(height-3):
        to_multiply = []
        for i in range(4):
            to_multiply.append(rows[start_row - i][start_col + i])
        if product_of(to_multiply) > left_diags:
            left_diags = product_of(to_multiply)
#assert left_diags == 10 ** 5

candidates.append(left_diags)

print(max(candidates))
