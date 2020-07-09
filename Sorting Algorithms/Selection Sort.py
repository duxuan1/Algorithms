from typing import List


def selection_sort(lst: List[int]) -> List[int]:
    """
    Find the largest element and making it the last element in the list.
    Make repeated passes until the list is sorted.
    """
    for iteration in range(len(lst)):
        largest = -float('inf')
        for index in range(len(lst) - iteration):
            if largest < lst[index]:
                largest = lst[index]
        lst[len(lst) - iteration - 1] = largest
    return lst


if __name__ == "__main__":
    lst = [5, 2, 7, 1, 9, 0]
    res = selection_sort(lst)
    assert res == sorted(lst)
