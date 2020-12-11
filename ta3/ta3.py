# Jake Underland


def next_in_pattern(lst):
    '''
    Finds the next number in the pattern, assuming the pattern
    is described by a polynomial whose degree is less than the
    length of the input list.

    Input:
        lst: list of numbers (of length at least one)

    Returns: The next number in the pattern.
    '''
    next_number = lst[-1]
    finite_dif = []
    for i, _ in enumerate(lst[:-1]):
        delta = lst[i+1] - lst[i]
        finite_dif.append(delta)
    if finite_dif[0] == finite_dif[1]:
        return next_number + finite_dif[-1]
    else: 
        return next_number + next_in_pattern(finite_dif)


