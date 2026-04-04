from functools import reduce

names = input().split()

longest = reduce(lambda a, b: a if len(a) > len(b) else b, names)

print(longest)
