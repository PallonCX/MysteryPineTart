def count(diff):
    num_set = set()
    left = 1
    for i in range(1, diff):
        while left in num_set:
            left += 1
        num_set.add(left)
        num_set.add(left + i)
        print("Diff: ", i, (left, left + i))

count(50)