import problem1D


def peakFinder1D(array):

    def bPeakFinder(array, low, high):
        if high == low:
            return array[low]
        mid = (low + high)//2

        if array[mid] > array[mid+1] and array[mid] > array[mid-1]:
            return array[mid]
        if array[mid] < array[mid + 1]:
            return bPeakFinder(array, mid + 1, high)
        else:
            return bPeakFinder(array, low, mid-1)

    if len(array) == 0:
        return None
    else:
        return bPeakFinder(array, 0, len(array)-1)


def main():

    # Use Problem1D to enter your test array
    array = problem1D.problemList
    peak = peakFinder1D(array)
    print(peak, " : is a peak")

main()