import sys
import csv

# Opening the csv file
f = open(sys.argv[1], "r")
csv = csv.reader(f)

# making the csv file ready to input
data = list(csv)
data.remove(data[0])

# performing permutations
result = [[]]
for pool in data:
    result = [x + [y] for x in result for y in pool]
# printing all the permutations
for i in range(0, len(result) - 1):
    print("".join(tuple(result[i])), end=", ")
print("".join(tuple(result[-1])))