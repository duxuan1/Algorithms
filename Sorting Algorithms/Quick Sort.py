from typing import List, Tuple


def quick_sort(lst: List[int]) -> List[int]:
    """
    Return a sorted list with the same elements as <lst>.
    break a list up (partition) into the part smaller than some
    value (pivot) and not smaller than that value, sort these parts, then
    recombine the list
    """
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    smaller, bigger = partition(pivot, lst[1:])
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


def partition(pivot: int, lst: List[int]) -> Tuple[List, List]:
    """
    break a list up (partition) into the part smaller than some
    value (pivot) and not smaller than that valu
    """
    smaller, bigger = [], []
    for i in range(len(lst)):
        if lst[i] < pivot:
            smaller.append(lst[i])
        else:
            bigger.append(lst[i])
    return smaller, bigger


def make_list(n: int) -> List[int]:
    """
    Return a random list of n ints.
    """
    import random
    res = list(range(n))
    random.shuffle(res)
    return res


if __name__ == '__main__':
    size = 1000
    for i in range(4):
        L = make_list(size)
        assert quick_sort(L) == sorted(L)
        size *= 2
