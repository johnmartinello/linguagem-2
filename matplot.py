num_map = {}
nums = [1, 1, 1, 2, 2, 3]
k = 2
for i in nums:
    if i in num_map:
        num_map[i] += 1
    else:
        num_map[i] = 1

num_map = sorted(num_map, key=num_map.get, reverse=True)

print(num_map[:k])
