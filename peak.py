import problem2D

class PeakProblem(object):
    """
    A class representing an instance of a peak-finding problem.
    """

    def __init__(self, array, bounds):
        """

        :param array: Problem matrix
        :param bounds: rows to include in this problem
        """

        (startRow, startCol, numRow, numCol) = bounds

        self.array = array
        self.bounds = bounds
        self.startRow = startRow
        self.startCol = startCol
        self.numRow = numRow
        self.numCol = numCol

    def get(self, location):
        """
        :param location: given by the pair (r, c)
        :return: the value of the array at the given location, offset by the
        coordinates (startRow, startCol).

        RUNTIME: O(1)
        """

        (r, c) = location
        if not (0 <= r and r < self.numRow):
            return 0
        if not (0 <= c and c < self.numCol):
            return 0
        return self.array[self.startRow + r][self.startCol + c]

    def getBetterNeighbor(self, location):
        """
        :param location: given by the pair (r, c)
        :return: better neighbor if it exists, otherwise return location (r, c)

        RUNTIME O(1)
        """

        (r, c) = location
        best = location

        if r - 1 >= 0 and self.get((r -1, c)) > self.get(best):
            best = (r - 1, c)
        if c - 1 >= 0 and self.get((r, c - 1)) > self.get(best):
            best = (r, c - 1)
        if r + 1 < self.numRow and self.get((r + 1, c)) > self.get(best):
            best = (r + 1, c)
        if c + 1 < self.numCol and self.get((r, c + 1)) > self.get(best):
            best = (r, c + 1)

        return best

    def getMaximum(self, locations):
        """
        :param locations: list of locations (r, c) to search for the greatest value
        :return: returns the location in the current problem with the greatest value.

        RUNTIME: O(len(locations))
        """

        (bestLoc, bestVal) = (None, 0)

        for loc in locations:
            if bestLoc is None or self.get(loc) > bestVal:
                (bestLoc, bestVal) = (loc, self.get(loc))

        return bestLoc

    def isPeak(self, location):
        """
        :param location: given by the pair (r, c)
        :return: True if the given location is a peak in the current subproblem.

        RUNTIME = O(1)
        """

        return (self.getBetterNeighbor(location) == location)

    def getSubproblem(self, bounds):
        """
        :param bounds: tuple of numbers: (starting row, starting col, # of rows, # of cols).
        :return: a subproblem with the given bounds.

        RUNTIME: O(1)
        """

        (sRow, sCol, nRow, nCol) = bounds
        newBounds = (self.startRow + sRow, self.startCol + sCol, nRow, nCol)
        return PeakProblem(self.array, newBounds)

    def getSubproblemContaining(self, boundList, location):
        """
        :param boundList: list of subproblems
        :param location: of item where the new subproblem is
        :return: the subproblem containing the given location
        """

        (row, col) = location
        for (sRow, sCol, nRow, nCol) in boundList:
            if sRow <= row and row < sRow + nRow:
                if sCol <= col and col < sCol + nCol:
                    return self.getSubproblem((sRow, sCol, nRow, nCol))

        # shouldn't reach here
        return self

    def getLocationInSelf(self, problem, location):
        """
        Remaps the location in the given problem to the same location in
        the problem that this function is being called from.

        :param problem:
        :param location:
        :return:
        """

        (row, col) = location
        newRow = row + problem.startRow - self.startRow
        newCol = col + problem.startCol - self.startCol
        return (newRow, newCol)

### Helper Methods ###

def getDimensions(array):
    """
    Gets the dimensions for a two-dimensional array.  The first dimension
    is simply the number of items in the list; the second dimension is the
    length of the shortest row.  This ensures that any location (row, col)
    that is less than the resulting bounds will in fact map to a valid
    location in the array.

    RUNTIME: O(len(array))

    """
    rows = len(array)
    cols = 0

    for row in array:
        if len(row) > cols:         # Review carefully
            cols = len(row)
    return (rows, cols)

def createProblem(array):
    """

    :param array:
    :return: an instance of the PeakProblem object for the given array using bounds derived
    from the array using getDimensions helper function.

    RUNTIME: O(len(array))
    """

    (rows, cols) = getDimensions(array)
    return PeakProblem(array, (0, 0, rows, cols))