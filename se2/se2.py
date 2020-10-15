def is_pythagorean_triple(a, b, c):
    """
    Do a, b, and c form a Pythagorean Triple?

    a, b, c: ints

    Returns: bool
    """

    ### EXERCISE 1 -- Replace pass with your code
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


def characterize_nums(lst):
    """
    Characterize a list by counting the number of negative
    numbers, zeros, and positive numbers.

    lst: list of ints

    Returns: (int, int, int)
    """

    ### EXERCISE 2 -- Replace pass with your code
    negative = 0
    zeros = 0
    positive = 0

    for i in lst:
        if i > 0:
            positive += 1
        elif i == 0:
            zeros += 1
        else:
            negative += 1

    return negative, zeros, positive
        



def compute_matching(lst1, lst2):
    """
    Given two lists of equal length, compute a list
    that where the ith element is True if the lists
    match at index i.

    lst1, lst2: lists

    Returns: list of bools
    """
    ### Leave this assertion
    assert len(lst1) == len(lst2)

    ### EXERCISE 3 -- Replace pass with your code
    new_lst = []

    for i, _ in enumerate(lst1):
        if lst1[i] == lst2[i]:
            new_lst.append(True)
        else:
            new_lst.append(False)
    
    return new_lst


def compute_matching_indices(lst1, lst2):
    """
    Given two lists of equal length, compute a list that of the
    indices where the two lists have the same value.

    lst1, lst2: lists

    Returns: list of integer indices
    """
    ### Leave this assertion
    assert len(lst1) == len(lst2)

    ### EXERCISE 4 -- Replace pass with your code
    new_lst = []

    for i, _ in enumerate(lst1):
        if lst1[i] == lst2[i]:
            new_lst.append(i)
    
    return new_lst


def destructive_negate(lst):
    """
    Negate the value of each element in the list *in place*.

    lst: list of ints
    """

    ### EXERCISE 5 -- Replace pass with your code
    for i, val in enumerate(lst):
        lst[i] = -val


def win_lose_or_draw(board, row, col):
    """
    Returns "Win", "Lose", or "Draw" depending on whether sum of the 
    values in the row is larger, smaller, or the same as the sum
    of the values in the column

    board: list of lists of ints
    row: int
    col: int

    Returns: string: "Win", "Lose", or "Draw"
    """

    ### EXERCISE 6 -- Replace pass with your code
    total_row = 0
    total_column = 0
    for i in board[row]:
        total_row = total_row + i
    for row in board:
        total_column = total_column + row[col]
    if total_row > total_column:
        return "Win"
    elif total_row == total_column:
        return "Draw"
    else:
        return "Lose"

