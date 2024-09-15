#!/usr/bin/python3
"""find the maximum integer in a list."""


def max_integer(nums):
    """Find and return the maximum integer in a list of integers.

    Args:
        nums (list): A list of integers. If the list is empty, returns None.

    Returns:
        int or None: maximum integer in the list, or None if the list is empty.
    """
    if not nums:
        return None

    # Initialize the maximum value to the first element in list
    maximum = nums[0]

    # Iterate over the list to find the maximum value
    for num in nums[1:]:
        if num > maximum:
            maximum = num

    return maximum
