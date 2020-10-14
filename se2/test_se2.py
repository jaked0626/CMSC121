import sys
import os

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se2

MODULE = "se2"

def test_is_pythagorean_triple_1():
    do_test_is_pythagorean_triple(a=4, b=3, c=5, expected=True)

def test_is_pythagorean_triple_2():
    do_test_is_pythagorean_triple(a=3, b=4, c=5, expected=True)

def test_is_pythagorean_triple_3():
    do_test_is_pythagorean_triple(a=3, b=4, c=6, expected=False)

def test_is_pythagorean_triple_4():
    # check that the code works for something other than the
    # given examples
    do_test_is_pythagorean_triple(a=5, b=12, c=13, expected=True)

def test_is_pythagorean_triple_5():
    # check that the code works for something other than the
    # given examples
    do_test_is_pythagorean_triple(a=6, b=12, c=13, expected=False)

def test_is_pythagorean_triple_5():
    # boundary case.
    do_test_is_pythagorean_triple(a=1, b=1, c=1, expected=False)

def test_characterize_nums_1():
    lst = [-1, -2, -3, 0, 0, 0, 1, 2, 3]
    do_test_characterize_nums(lst=lst, expected=(3,3,3))
    
def test_characterize_nums_2():
    lst = [-1, -2, -3]
    do_test_characterize_nums(lst=lst, expected=(3,0,0))

def test_characterize_nums_3():
    lst = [0, 0, 0]
    do_test_characterize_nums(lst=lst, expected=(0,3,0))

def test_characterize_nums_4():
    lst = [1, 2, 3]
    do_test_characterize_nums(lst=lst, expected=(0,0,3))

def test_characterize_nums_4():
    lst = []
    do_test_characterize_nums(lst=lst, expected=(0,0,0))
                              
def test_characterize_nums_5():
    lst = [-2, 0, 1, -1]
    do_test_characterize_nums(lst=lst, expected=(2, 1, 1))

def test_characterize_nums_6():
    lst = [2, 0, 1, -1, 7, 27, 0, 0, 0, -10]
    do_test_characterize_nums(lst=lst, expected=(2, 4, 4))

def test_compute_matching_values_1():
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    do_test_compute_matching(lst1=lst1, lst2=lst2, expected=[True, True, True])

def test_compute_matching_values_2():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    do_test_compute_matching(lst1=lst1, lst2=lst2, expected=[False, False, False])

def test_compute_matching_values_3():
    lst1 = [1, 2, 3]
    lst2 = [4, 2, 6]
    do_test_compute_matching(lst1=lst1, lst2=lst2, expected=[False, True, False])

def test_compute_matching_values_4():
    lst1 = ["a", "b"]
    lst2 = ["a", "B"]
    do_test_compute_matching(lst1=lst1, lst2=lst2, expected=[True, False])

def test_compute_matching_values_5():
    lst1 = ["1", 2, [1, 2]]
    lst2 = [1, 7, [1, 2]]
    do_test_compute_matching(lst1=lst1, lst2=lst2, expected=[False, False, True])

def test_compute_matching_values_6():
    lst1 = []
    lst2 = []
    do_test_compute_matching(lst1=lst1, lst2=lst2, expected=[])


def test_compute_matching_indices_1():
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    do_test_compute_matching_indices(lst1=lst1, lst2=lst2, expected=[0, 1, 2])

def test_compute_matching_indices_2(): 
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    do_test_compute_matching_indices(lst1=lst1, lst2=lst2, expected=[])

def test_compute_matching_indices_3(): 
    lst1 = [1, 2, 3]
    lst2 = [4, 2, 6]
    do_test_compute_matching_indices(lst1=lst1, lst2=lst2, expected=[1])

def test_compute_matching_indices_4():
    lst1 = ["A", "b"]
    lst2 = ["A", "B"]
    do_test_compute_matching_indices(lst1=lst1, lst2=lst2, expected=[0])

def test_compute_matching_indices_5():
    lst1 = ["1", 2, [1, 2]]
    lst2 = [1, 7, [1, 2]]
    do_test_compute_matching_indices(lst1=lst1, lst2=lst2, expected=[2])

def test_compute_matching_indices_6():
    lst1 = []
    lst2 = []
    do_test_compute_matching_indices(lst1=lst1, lst2=lst2, expected=[])

def test_destructive_negate_1():
    do_test_destructive_negate(lst=[1, 2, 3, 4], expected=[-1, -2, -3, -4])

def test_destructive_negate_2():
    do_test_destructive_negate(lst=[-1, -2, -3, -4], expected=[1, 2, 3, 4])

def test_destructive_negate_3():
    do_test_destructive_negate(lst=[-1, 2, -3, 4], expected=[1, -2, 3, -4])

def test_destructive_negate_4():
    do_test_destructive_negate(lst=[], expected=[])
    




board1 = [[3, 2, 3, 2, 10],
          [3, 2, 2, 3, 2],
          [3, 2, 2, 2, 2],
          [3, 2, 2, 2, 2],
          [3, 3, 3, 3, 3]]

board2 = [[3, 2, 3, 2],
          [3, 2, 2, 3],
          [3, 2, 2, 2],
          [3, 2, 2, 10],
          [3, 3, 3, 3]]

def test_win_lose_or_draw1():
    do_test_win_lose_or_draw(board=board1, row=0, col=4, expected="Win")

def test_win_lose_or_draw2():
    do_test_win_lose_or_draw(board=board1, row=4, col=3, expected="Win")

def test_win_lose_or_draw3():
    do_test_win_lose_or_draw(board=board1, row=2, col=2, expected="Lose")

def test_win_lose_or_draw4():
    do_test_win_lose_or_draw(board=board1, row=1, col=2, expected="Draw")

def test_win_lose_or_draw5():
    do_test_win_lose_or_draw(board=board2, row=4, col=1, expected="Win")

def test_win_lose_or_draw6():
    do_test_win_lose_or_draw(board=board2, row=0, col=2, expected="Lose")

def test_win_lose_or_draw7():
    do_test_win_lose_or_draw(board=board2, row=4, col=2, expected="Draw")


# # #
#
# HELPER FUNCTIONS
#
# # #

def gen_recreate_msg(module, function, *params):
    params_str = ", ".join([str(p) for p in params])

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg


def check_none(actual, recreate_msg=None):
    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_expected_none(actual, recreate_msg=None):
    msg = "The function is expected to return None."
    msg += " Your function returns: {}".format(actual)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg


def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg


def check_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    msg = "You modified the contents of {} (this is not allowed).\n".format(param_name)
    msg += "  Value before your code: {}\n".format(before)
    msg += "  Value after your code:  {}".format(after)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert before == after, msg


# # #
#
# TEST HELPERS
#
# # #


def do_test_is_pythagorean_triple(a, b, c, expected):
    recreate_msg = gen_recreate_msg(MODULE, "is_pythagorean_triple", *(a, b, c))

    actual = se2.is_pythagorean_triple(a, b, c)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_characterize_nums(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "characterize_nums", *(lst,))

    actual = se2.characterize_nums(lst)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_compute_matching(lst1, lst2, expected):
    recreate_msg = gen_recreate_msg(MODULE, "compute_matching", *(lst1, lst2))

    actual = se2.compute_matching(lst1, lst2)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_compute_matching_indices(lst1, lst2, expected):
    recreate_msg = gen_recreate_msg(MODULE, "compute_matching_indices", *(lst1, lst2))

    actual = se2.compute_matching_indices(lst1, lst2)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_destructive_negate(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "destructive_negate", *(lst,))

    lst_copy = lst[:]
    actual = se2.destructive_negate(lst_copy)

    check_expected_none(actual, recreate_msg)
    check_equals(lst_copy, expected, recreate_msg)


def do_test_win_lose_or_draw(board, row, col, expected):
    recreate_msg = "  board = {}".format(board)
    recreate_msg += gen_recreate_msg(MODULE, "win_lose_or_draw", *("board", row, col))

    actual = se2.win_lose_or_draw(board, row, col)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    


    
