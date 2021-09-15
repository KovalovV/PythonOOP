def countMaxWeigth(weigth, values, capacity):
    """Builds a matrix of possible sets of backpacks and returns the most profitable"""
    arrayOfBag = [[0] * (capacity + 1) for _ in range(len(weigth) + 1)]
    for i in range(len(arrayOfBag)):
        for j in range(len(arrayOfBag[i])):
            arrayOfBag[i][j] = 0
    for i in range(len(arrayOfBag)):
        for j in range(len(arrayOfBag[i])):
            if j == 0 or i == 0:
                arrayOfBag[i][j] = 0
            else:
                if weigth[i - 1] > j:
                    arrayOfBag[i][j] = arrayOfBag[i - 1][j]
                else:
                    lastOfPrevRow = arrayOfBag[i - 1][j]
                    oneOfTheMax = values[i - 1] + arrayOfBag[i - 1][j - weigth[i - 1]]
                    arrayOfBag[i][j] = max(lastOfPrevRow, oneOfTheMax)
    for i in range(len(arrayOfBag)):
        for j in range(len(arrayOfBag[i])):
            print('{:5}'.format(arrayOfBag[i][j]), end = ' ')
        print()
    return arrayOfBag[len(weigth)][capacity]


weigth = [2, 5, 3]
values = [100, 250, 300]
print(countMaxWeigth(weigth, values, 5))