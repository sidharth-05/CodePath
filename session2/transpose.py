def main():
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    print(transpose(matrix))

    matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
    print(transpose(matrix))

def transpose(matrix):
    # Print the transpose of the matrix 
    result_matrix = []
    for i in range(len(matrix[0])):
        result_row = []
        for j in range(len(matrix)):
            result_row.append(matrix[j][i])
        result_matrix.append(result_row)
    return result_matrix

if __name__ == "__main__":
    main()