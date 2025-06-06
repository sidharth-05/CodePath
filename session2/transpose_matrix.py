def main():
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    print(transpose(matrix))

    matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
    print(transpose(matrix))

def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        rows = []
        for j in range(len(matrix)):
            rows.append(matrix[j][i])
        result.append(rows)
    return result



if __name__ == '__main__':
    main()