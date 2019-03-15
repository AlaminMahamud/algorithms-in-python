"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
------------------------------
Input: List, N
Output: List
"""


def delete_nth_naive(input, n):  # Time complexity O(n^2)

    output = []
    for i in input:
        if output.count(i) < n:
            output.append(i)
    return output


def delete_nth(input, n):  # Time Complexity O(n), using hash tables.

    output = []
    import collections
    counts = collections.defaultdict(int)

    for i in input:
        if counts[i] < n:
            output.append(i)
            counts[i] += 1

    return output


if __name__ == "__main__":
    input = [1, 2, 3, 1, 2, 1, 2, 3]
    print(input)
    output = delete_nth_naive(input, 2)
    print(output)
    print("--------------------------")

    print(input)
    outputV2 = delete_nth(input, 2)
    print(output)
