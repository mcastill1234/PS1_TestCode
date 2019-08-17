import random


def randomProblem(rows = 10, columns = 10, max = 100):
    """
    :param rows: number of rows
    :param columns: number of columns
    :param max: max value that each number can take
    :return: random matrix of rows x columns. Each number is distributed uniformly at random between
    zero and max.
    """

    result = []

    for i in range(rows):
        resultRow = []

        for j in range(columns):
            resultRow.append(random.randint(0, max))

        result.append(resultRow)

    return result
