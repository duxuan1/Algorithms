from typing import List


def selection_sort(lst: List[int]) -> List[int]:
    """
    Find the largest element and making it the last element in the list.
    Make repeated passes until the list is sorted.
    """
    for iteration in range(len(lst)):
        smallest_index = iteration
        for index in range(smallest_index, len(lst)):
            if lst[index] < lst[smallest_index]:
                smallest_index = index
        lst[iteration], lst[smallest_index] = lst[smallest_index], lst[iteration]
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
        assert selection_sort(L) == sorted(L)
        size *= 2
