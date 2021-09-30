def count_max_weigth(weigth, values, capacity):
    """Builds a matrix of possible sets of backpacks and returns the most profitable"""


    matrix_of_bag = [[0 for _ in range(capacity + 1)] for _ in range(len(weigth) + 1)]
    for i in range(len(matrix_of_bag)):
        for j in range(len(matrix_of_bag[i])):
            if not j or not i:
                matrix_of_bag[i][j] = 0
            else:
                if weigth[i - 1] > j:
                    matrix_of_bag[i][j] = matrix_of_bag[i - 1][j]
                else:
                    last_of_prev_row = matrix_of_bag[i - 1][j]
                    one_of_the_max = values[i - 1] + matrix_of_bag[i - 1][j - weigth[i - 1]]
                    matrix_of_bag[i][j] = max(last_of_prev_row, one_of_the_max)
    return matrix_of_bag[len(weigth)][capacity]


weigth = [29, 10, 10, 10]
values = [29, 10, 10, 10]
print(count_max_weigth(weigth, values, 30))