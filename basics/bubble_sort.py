# Author: Allen Anker
# Created by Allen Anker on 09/10/2018


# procedure bubbleSort( A : list of sortable items )
def bubble_sort(a):
    """
    Bubble sort.
    :param a: A list of number
    :return: In-place sort for list a
    """
    # n = length(A)
    n = len(a)
    # repeat util the whole list is in the sorted part
    while n > 1:
        # for i = 1 to n-1 inclusive do
        for i in range(1, n):
            # if this pair is out of order
            # if A[i-1] > A[i] then
            if a[i - 1] > a[i]:
                # swap them and remember something changed
                # swap( A[i-1], A[i] )
                a[i - 1], a[i] = a[i], a[i - 1]
        # the sorted part increments by 1 when the current biggest is transferred to the right sorted part
        n -= 1


if __name__ == '__main__':
    a = [2, 3, 1, 5, 7, 6]
    bubble_sort(a)
    print(a)
