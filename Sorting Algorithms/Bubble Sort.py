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


if __name__ == "__main__":
    lst = [5, 2, 7, 1, 9, 0]
    res = bubble_sort(lst)
    assert res == sorted(lst)
