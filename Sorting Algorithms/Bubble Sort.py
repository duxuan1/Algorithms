from typing import List


def bubble_sort(lst: List[int]) -> List[int]:
    """
    Iterate through the list swapping the larger element move forward when swapping.
    In the other words, larger elements bubble to the top.
    Make repeated passes until the list is sorted.
    Time Complexity: O(n^2) in average and O(n) in best
    Space Complexity: O(1)
    """
    for iteration in range(len(lst)):
        for index in range(len(lst) - 1 - iteration):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
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
        assert bubble_sort(L) == sorted(L)
        size *= 2
