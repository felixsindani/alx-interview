#!/usr/bin/python3
'''fnct returns the perimeter of the island described in grid'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0
    Indx_last_list = len(grid) - 1  # index of the last list in the grid
    Indx_last_sqr_list = len(grid[0]) - 1  # index of the last square in list

    for first_index, lst in enumerate(grid):
        for land_index, land in enumerate(lst):
            if land == 1:  # left and right
                if land_index == 0:  # left side
                    counter += 1  # right side
                    if lst[land_index + 1] == 0:
                        counter += 1
                elif land_index == Indx_last_sqr_list:  # left side
                    if lst[land_index - 1] == 0:
                        counter += 1  # right side
                    counter += 1
                else:
                    # left side
                    if lst[land_index - 1] == 0:
                        counter += 1

                    # right side
                    if lst[land_index + 1] == 0:
                        counter += 1

                # top and down
                if first_index == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[first_index + 1][land_index] == 0:
                        counter += 1
                elif first_index == Indx_last_list:
                    # top side
                    if grid[first_index - 1][land_index] == 0:
                        counter += 1  
                        # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[first_index - 1][land_index] == 0:
                        counter += 1

                    # bottom side
                    if grid[first_index + 1][land_index] == 0:
                        counter += 1

    return counter


