matrix = []
n, m = map(int, input().split())
#m = int(input())
for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

transposed_matrix = [[0 for i in range(n)] for j in range(m)]
'''
for i in range(n):
    for j in range(m):
        transposed_matrix[j][i] = matrix[i][j]
'''

transposed_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]        
for i in range(m):
    for j in range(n):
        print(transposed_matrix[i][j], end = " ")
    print()

