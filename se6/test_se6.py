import sys
import os

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se6
import util
from tree import Tree

MODULE = "se6"

# # #
#
# HELPER FUNCTIONS
#
# # #

def check_none(actual, recreate_msg=None):
    msg = "The method returned None."
    msg += " Did you forget a return statement?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_expected_none(actual, recreate_msg=None):
    msg = "The method is expected to return None."
    msg += " Your method returns: {}".format(actual)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg

def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The method returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_attribute(actual, attribute_name, recreate_msg=None):
    msg = "Your class should have a '{}' attribute.".format(attribute_name)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert hasattr(actual, attribute_name), msg

def check_attribute_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "Your class has an attribute of the wrong type.\n"
    msg += "  Expected type: {}.\n".format(expected_type.__name__)
    msg += "  Actual type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_equals(actual, expected, recreate_msg=None):
    msg = ("Actual ({}) and expected ({}) values " 
        "do not match.").format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg

def pretty_print_repr(x):
    return repr(x)

def gen_recreate_msg(module, function, *params, **kwparams):
    params_str = ", ".join([pretty_print_repr(p) for p in params])
    if len(kwparams) > 0:
        params_str += ", ".join(["{} = {}".format(k, repr(v)) 
            for k, v in kwparams.items()])
    lines = ["{}.{}({})".format(module, function, params_str)]
    return gen_recreate_msg_by_lines(lines)

def gen_recreate_msg_with_trees(module, function, tree_name):
    lines = ['import util',
             'trees = util.load_trees("sample_trees.json")',
             '{}.{}(trees["{}"])'.format(module, function, tree_name)]
    return gen_recreate_msg_by_lines(lines)

def gen_recreate_msg_by_lines(lines):
    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  " + "\n  ".join(lines)
    return recreate_msg

# # #
#
# TEST HELPERS
#
# # #

def do_test_sum_cubes(n):
    recreate_msg = gen_recreate_msg(MODULE, 'sum_cubes', n)
    actual = se6.sum_cubes(n)
    expected = sum(n ** 3 for n in range(n + 1))
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_sublists(lst):
    recreate_msg = gen_recreate_msg(MODULE, 'sublists', lst)
    actual = se6.sublists(lst)
    expected = [[x for j, x in enumerate(lst) if i ^ (2 ** j) < i] 
        for i in range(2 ** len(lst))]
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    for el in actual:
        check_type(el, [], recreate_msg)
    check_equals(sorted(actual), sorted(expected), recreate_msg)

def do_test_min_depth_leaf(tree_name, expected):
    recreate_msg = gen_recreate_msg_with_trees(
        MODULE, 'min_depth_leaf', tree_name)
    actual = se6.min_depth_leaf(trees[tree_name])
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

def do_test_repeated_value(tree_name, expected):
    recreate_msg = gen_recreate_msg_with_trees(
        MODULE, 'repeated_value', tree_name)
    actual = se6.repeated_value(trees[tree_name])
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)

# # #
#
# TESTS
#
# # #

def test_sum_cubes_1():
    do_test_sum_cubes(3)

def test_sum_cubes_2():
    do_test_sum_cubes(9)

def test_sum_cubes_3():
    do_test_sum_cubes(0)

def test_sum_cubes_4():
    do_test_sum_cubes(50)

def test_sum_cubes_5():
    do_test_sum_cubes(81)

def test_sublists_1():
    do_test_sublists(['A', 'B', 'C', 'D'])

def test_sublists_2():
    do_test_sublists([50, 0, -1, 10])

def test_sublists_3():
    do_test_sublists([True])

def test_sublists_4():
    do_test_sublists(['U', 'V', 'W', 'X', 'Y', 'Z'])

def test_sublists_5():
    do_test_sublists(list(range(0, 70, 10)))

def test_min_depth_leaf_1():
    do_test_min_depth_leaf("tree_1", 1)

def test_min_depth_leaf_2():
    do_test_min_depth_leaf("tree_2", 1)

def test_min_depth_leaf_3():
    do_test_min_depth_leaf("tree_3", 5)
    
def test_min_depth_leaf_4():
    do_test_min_depth_leaf("tree_4", 4)
    
def test_min_depth_leaf_5():
    do_test_min_depth_leaf("tree_5", 3)

def test_repeated_value_1():
    do_test_repeated_value("tree_1", False)

def test_repeated_value_2():
    do_test_repeated_value("tree_2", True)

def test_repeated_value_3():
    do_test_repeated_value("tree_3", False)

def test_repeated_value_4():
    do_test_repeated_value("tree_4", False)

def test_repeated_value_5():
    do_test_repeated_value("tree_5", True)

# # #
#
# TEST TREES
#
# # #

trees = util.load_trees("sample_trees.json")