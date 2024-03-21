#!/usr/bin/python3
'''method that calculates the fewest number of operations needed to result in exactly n H characters in the file.'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chars = 1
    # no of chars in the file
    clipboard = 0 
    # no of H's copied
    counter = 0
    # operations counter

    while pasted_chars < n:
        # if nothing was copied
        if clipboard == 0:
            # copy all
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if nothing is pasted
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chars
        # remaining chars to Paste
        # check if impossible
        # by checking if clipboard
        # has more than needed to reach desired number
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars # copy all and paste
            pasted_chars += clipboard
            counter += 2

    # if desired result is found
    if pasted_chars == n:
        return counter
    else:
        return 0
