import sys
dimensions = map(int, raw_input().split())
matrix = [map(int, row.split()) for row in sys.stdin]
column_num = matrix.pop()[0]
matrix = sorted(matrix, key=lambda x: x[column_num])

for row in matrix:
    print " ".join(str(x) for x in row)
