


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_list = [x for row in matrix for x in row]


check = [[ 0 for _ in range(5)] for _ in range(5) ]