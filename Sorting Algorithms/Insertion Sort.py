from typing import List


def insertion_sort(lst: List[int]) -> List[int]:
    """
    Inserts the next item in the "unsorted" part of the list into the correct place
    in the sorted section of the list.
    """
    if len(lst) <= 1:
        return lst
    for iteration in range(1, len(lst)):
        for index in range(0, iteration + 1):
            if lst[index] > lst[iteration]:
                lst[index], lst[iteration] = lst[iteration], lst[index]
    return lst


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
        assert insertion_sort(L) == sorted(L)
        size *= 2