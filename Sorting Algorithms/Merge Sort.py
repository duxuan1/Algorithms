from typing import List


def merge(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return a new list that contains the items in L1 and L2 in
    non-descending order. L1 and L2 are both already in that order.
    """
    merged = []
    index1, index2 = 0, 0
    # merge the two lists until one is empty
    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] < l2[index2]:
            merged.append(l1[index1])
            index1 += 1
        else:
            merged.append(l2[index2])
            index2 += 1
    # If a list is empty, it doesn't change the accumulated list if we add it.
    merged += l1[index1:]
    merged += l2[index2:]
    return merged


def merge_sort(lst: List[int]) -> List[int]:
    """
    Return a list that contains the items in L in non-descending order.
    """
    # Base case
    if len(lst) < 2:
        return lst
    # Recursive case
    mid = len(lst) // 2
    l1 = merge_sort(lst[:mid])
    l2 = merge_sort(lst[mid:])
    return merge(l1, l2)


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
        assert merge_sort(L) == sorted(L)
        size *= 2
