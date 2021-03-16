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
        i = partition(pivot, lst, left, right - 1)
        lst[i], lst[right] = lst[right], lst[i]
        quick_sort(lst, left, i - 1)
        quick_sort(lst, i + 1, right)


def partition(pivot: int, lst: List[int], left: int, right: int):
    """
    break a list up (partition) into the part smaller than some
    value (pivot) and not smaller than that valu
    """
    i = j = left
    while j <= right:
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1
    return i


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
