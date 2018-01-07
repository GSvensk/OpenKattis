def smash_sideways(left, row):
    
    if left:
        counter = 0
        # for each position in row
        while counter != 3:
            tmp = counter + 1
            
            # loop through zeroes
            while (tmp < 3) & (row[tmp] == 0):
                tmp += 1
            
            # if it's possible to smash together
            if row[counter] == row[tmp]:
                row[counter] = 2 * row[counter]
                row[tmp] = 0
            # else move down and try again
            elif row[counter] == 0:
                row[counter] = row[tmp]
                row[tmp] = 0
                counter -= 1

            counter += 1
    #smash right
    else:
        counter = 3
        # for each position in row
        while counter != 0:
            tmp = counter - 1

            # loop through zeroes
            while (tmp > 0) & (row[tmp] == 0):
                tmp -= 1
            
            # if smashable
            if row[counter] == row[tmp]:
                row[counter] = 2 * row[counter]
                row[tmp] = 0
    
            # else move down and try again
            elif row[counter] == 0:
                row[counter] = row[tmp]
                row[tmp] = 0
                counter += 1

            counter -= 1

    return row


def rotate_matrix(n, matrix):

    for x in range(int(n/2)):
        for y in range(x, n-x-1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = tmp

    return matrix


if __name__ == '__main__':

    matrix = [[0 for x in range(4)] for y in range(4)]

    for i in range(4):
        matrix[i] = list(map(int, input().split()))

    direction = int(input())

    if direction == 0:
        for i in matrix:
            i = smash_sideways(True, i)
    elif direction == 1:
        matrix = rotate_matrix(4, matrix)
        for i in matrix:
            i = smash_sideways(True, i)
        matrix = rotate_matrix(4, matrix)
        matrix = rotate_matrix(4, matrix)
        matrix = rotate_matrix(4, matrix)
    elif direction == 2:
        for i in matrix:
            i = smash_sideways(False, i)

    elif direction == 3:
        matrix = rotate_matrix(4, matrix)
        for i in matrix:
            i = smash_sideways(False, i)
        matrix = rotate_matrix(4, matrix)
        matrix = rotate_matrix(4, matrix)
        matrix = rotate_matrix(4, matrix)

    # print matrix
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end = " ")
        print()
