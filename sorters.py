"""
Pure python implementation of different sorting algorithms.
"""
from random import randint


def bubble_sort(array):
    """Sort according to bubble sort method.

    Args:
        array: an array_like to sort.

    Returns:
        The sorted array_like.
    """
    n = len(array)
    for i in range(n):
        # Flag to terminate early if there's nothing left to sort
        already_sorted = True

        # Look at each item one by one, comparing it with its adjacent value. With each
        # iteration, the portion of the array_like that you look at shrinks because the remaining
        # items have already been sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its adjacent value, then swap them
                # and set `already_sorted` to `False` so the algorithm doesn't finish prematurely
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        # If there were no swaps during the last iteration, the array_like is already sorted,
        # and you can terminate
        if already_sorted:
            break
    return array


def insertion_sort(array, left=0, right=None):
    """Sort according to insertion sort method.

    Args:
        array: an array_like to sort.
        left: reference element for start looping.
        right: reference element for end of looping.

    Returns:
        The sorted array_like.
    """
    right = len(array) - 1 if right is None else right

    # Loop from `left` element to `right` element
    for i in range(left + 1, right + 1):
        # `key_item` is the element we want to insert in its correct place
        key_item = array[i]

        # Initialize variable used to find the correct position of `key_item`
        j = i - 1

        # Run through the left portion of the array_like and find the correct position of `key_item`.
        # Only if `key_item` is smaller than its adjacent values.
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left and reposition `j` to point to the next
            # element (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # After shifting all the elements, position `key_item` in its correct location
        array[j + 1] = key_item
    return array


def _merge(left, right):
    """Merge functionality for the merge sort algorithm.

    Args:
        left: an array_like.
        right: an array_like.

    Returns:
        The arrays merged in a sorted way.
    """
    # If one array_like is empty, there is nothing to merge, return the other array_like
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    # Go through both arrays until all the elements make it into the resultant array_like
    while len(result) < len(left) + len(right):
        # Sort elements as we add them to `result`. Need to decide whether to get the next element
        # from the first or the second array_like
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        # If we reach the end of either array_like, add the remaining elements from the  other array_like to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    """Sort according to merge sort method.

    Args:
        array: an array_like to sort.

    Returns:
        The sorted array_like.
    """
    # If input array_like contains less than two elements, return it
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    # Recursively split the input into two equal halves, sorting each and merging them into the
    # final result
    return _merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


def quicksort(array):
    """Sort according to quick sort method.

    Args:
        array: an array_like to sort.

    Returns:
        The sorted array_like.
    """
    # If input array_like contains less than two elements, return it
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]  # select `pivot` element randomly

    for item in array:
        # Elements smaller than `pivot` go to the `low` list. Elements larger `pivot` go to the
        # `high` list. Elements equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # Final result combines the sorted `low` list with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


def timsort(array):
    """Sort according to tim sort method.

    Args:
        array: an array_like to sort.

    Returns:
        The sorted array_like.
    """
    min_run = 32
    n = len(array)

    # Slice & sort small portions of the input array_like. Slice size is defined by `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Merge the sorted slices from `min_run`, doubling the size of each iteration until we
    # surpass the length of the array_like.
    size = min_run
    while size < n:
        # Determine the arrays that will be merged together
        for start in range(0, n, size * 2):
            midpoint = start + size - 1  # first array_like's end & the second's start
            end = min((start + size * 2 - 1), (n - 1))  # second array_like's end

            # Merge the two subarrays. The `left` array should go from `start` to `midpoint + 1`,
            # while the `right` array_like should go from `midpoint + 1` to `end + 1`.
            merged_array = _merge(
                left=array[start : midpoint + 1], right=array[midpoint + 1 : end + 1]
            )

            # Put the merged array_like back into your array_like
            array[start : start + len(merged_array)] = merged_array
        # Each iteration should double the size of your arrays
        size *= 2
    return array
