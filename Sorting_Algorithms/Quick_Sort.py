from typing import List, Tuple
import random


def quick_sort(lst: List[int], left, right):
    """
    Return a sorted list with the same elements as <lst>.
    break a list up (partition) into the part smaller than some
    value (pivot) and not smaller than that value, sort these parts, then
    recombine the list
    """
    if left < right:
        pivot = lst[right]
        pivot_idx = partition(pivot, lst, left, right)

        quick_sort(lst, left, pivot_idx - 1)
        quick_sort(lst, pivot_idx + 1, right)


def partition(pivot: int, lst: List[int], left: int, right: int):
    """
    break a list up (partition) into the part smaller than some
    value (pivot) and not smaller than that value
    """
    actual_idx = left
    for i in range(left, right):
        if lst[i] < pivot:
            lst[i], lst[actual_idx] = lst[actual_idx], lst[i]
            actual_idx += 1
    lst[actual_idx], lst[right] = lst[right], lst[actual_idx]
    return actual_idx


def make_list(n: int) -> List[int]:
    """
    Return a random list of n ints.
    """
    import random
    res = list(range(n))
    random.shuffle(res)
    return res


if __name__ == '__main__':
    size = 5
    for _ in range(1):
        L = make_list(size)
        quick_sort(L, 0, len(L) - 1)
        assert L == sorted(L)
        size *= 5
