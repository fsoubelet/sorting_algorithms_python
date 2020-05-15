"""
Comparing the efficiency of different algorithms.
"""

from random import randint
from timeit import repeat

from sorters import bubble_sort, insertion_sort, merge_sort, quicksort, timsort

ARRAY_LENGTH = 10_000


def run_sorting_algorithm(algorithm, array_like):
    """
    Benchmark the execution efficiency of

    Args:
        algorithm: which algorithm to use for the sorting.
        array_like: the array to sort.

    Returns:
        Nothing, outputs statistic on runtime.
    """
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
    statement = f"{algorithm}({array_like})"

    execution_times = repeat(setup=setup_code, stmt=statement, repeat=3, number=10)
    print(f"Algorithm: {algorithm} - Minimum execution time: {min(execution_times):.6f} seconds")


if __name__ == '__main__':
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(f"Benchmarking on an array of size {ARRAY_LENGTH}")

    run_sorting_algorithm(algorithm="insertion_sort", array_like=array)
    run_sorting_algorithm(algorithm="merge_sort", array_like=array)
    run_sorting_algorithm(algorithm="quicksort", array_like=array)
    run_sorting_algorithm(algorithm="timsort", array_like=array)
    run_sorting_algorithm(algorithm="sorted", array_like=array)
