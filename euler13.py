nums = []
with open("big_sum.txt", 'r') as file:
    for line in file:
        nums.append(int(line))

print(str(sum(nums))[:10])