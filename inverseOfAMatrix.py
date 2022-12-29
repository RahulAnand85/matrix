n = int(input())
matrix = [[int(input()) for i in range(n)] for i in range(n)]
transpose = [[matrix[i][j] for i in trange(n)] for j in range(n)]

for i in matrix:
    print(i)

for i in transpose:
    print(i)

new = {transpose[i][j]: matrix[i][j]+i for j in range(n)}
print(new)