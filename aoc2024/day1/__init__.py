from pathlib import Path

# Read the input data and split it into two lists.
# Sample Data:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
input_file = Path(__file__).parent / "data.txt"
list_one = []
list_two = []


for line in input_file.open():
    left, right = map(int, line.split())
    list_one.append(left)
    list_two.append(right)

# We'll go through each list and find the minimum of each list and find the difference. Then we'll
# add these distances to a total distance. As we find the minimum, we'll remove the minimums and
# go through it again.
total_distance = 0
while list_one:
    min_one = min(list_one)
    min_two = min(list_two)
    total_distance += abs(min_one - min_two)
    list_one.remove(min_one)
    list_two.remove(min_two)

# WEEEEE!!!
print("Total Distance:", total_distance)