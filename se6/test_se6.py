import sys
import os
import pytest

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

def check_parameter_unmodified(actual, expected, param, recreate_msg=None):
    msg = ("Parameter {} has been modified:\n"
        "Actual ({}) and original ({}) values of {}" 
        "do not match.").format(param, param, actual, expected)
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

def check_tree_unmodified(t, expected_t, recreate_msg):
    expected_attributes = vars(expected_t)

    node_error_prefix = "Checking a node with " + ", ".join(
        ["{}={}".format(attr, repr(getattr(t, attr, "[not assigned]")))
        for attr in expected_attributes if attr != 'children']) + \
        "\nTree has been modified:\n"

    for attr in expected_attributes:
        assert hasattr(t, attr), \
            node_error_prefix + \
            "Node is missing attribute {}.\n".format(attr) + \
            recreate_msg

        if attr != 'children':
            assert getattr(t, attr) == getattr(expected_t, attr), \
            node_error_prefix + ("Node has incorrect {}. "
                "Got {}, expected {}.\n").format(attr,
                repr(getattr(t, attr)), repr(getattr(expected_t, attr))) + \
                recreate_msg
    
    expected_attributes_set = set(expected_attributes.keys())
    actual_attributes_set = set(vars(t).keys())
    assert actual_attributes_set == expected_attributes_set, \
            node_error_prefix + \
            "Node has extra attributes {}.\n".format(
                ", ".join(actual_attributes_set - expected_attributes_set)) + \
            recreate_msg


    children = list(t.children)
    expected_children = list(expected_t.children)

    if expected_children == []:
        assert children == [], node_error_prefix + \
            "Expected node to have no children, but it has children.\n" + \
            recreate_msg
    else:
        for c in children:
            assert isinstance(c, Tree), node_error_prefix + \
                "Node has a child that is not a Tree: {}\n".format(c) + \
                recreate_msg

        # This assumes no node has two children with the same key
        sorted_children = sorted(children, key=lambda st: st.key)
        sorted_expected_children = sorted(
            expected_children, key=lambda st: st.key)
        keys = [c.key for c in sorted_children]
        expected_keys = [c.key for c in sorted_expected_children]


        assert keys == expected_keys, node_error_prefix + \
            "Expected node to have children with keys {} " \
            "but the children's keys are {}.\n".format(expected_keys, keys) + \
            recreate_msg

        for child, expected_child in zip(sorted_children,
                                         sorted_expected_children):
            check_tree_unmodified(child, expected_child, recreate_msg)

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
    original_lst = list(lst)
    recreate_msg = gen_recreate_msg(MODULE, 'sublists', original_lst)
    expected = [[x for j, x in enumerate(lst) if i ^ (2 ** j) < i] 
        for i in range(2 ** len(lst))]
    actual = se6.sublists(lst)
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    for el in actual:
        check_type(el, [], recreate_msg)
    check_equals(sorted(actual), sorted(expected), recreate_msg)
    check_parameter_unmodified(lst, original_lst, "lst", recreate_msg)

def do_test_min_depth_leaf(trees_and_original_trees, tree_name, expected):
    trees, original_trees = trees_and_original_trees
    recreate_msg = gen_recreate_msg_with_trees(
        MODULE, 'min_depth_leaf', tree_name)
    actual = se6.min_depth_leaf(trees[tree_name])
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_tree_unmodified(trees[tree_name], original_trees[tree_name], 
                          recreate_msg)

def do_test_repeated_value(trees_and_original_trees, tree_name, expected):
    trees, original_trees = trees_and_original_trees
    recreate_msg = gen_recreate_msg_with_trees(
        MODULE, 'repeated_value', tree_name)
    actual = se6.repeated_value(trees[tree_name])
    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_tree_unmodified(trees[tree_name], original_trees[tree_name], 
                          recreate_msg)

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
    pass

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

def test_min_depth_leaf_1(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_1", 1)

def test_min_depth_leaf_2(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_2", 1)

def test_min_depth_leaf_3(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_3", 5)
    
def test_min_depth_leaf_4(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_4", 4)
    
def test_min_depth_leaf_5(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_5", 3)

def test_repeated_value_1(trees_repeated_value):
    do_test_repeated_value(trees_repeated_value, "tree_1", False)

def test_repeated_value_2(trees_repeated_value):
    do_test_repeated_value(trees_repeated_value, "tree_2", True)

def test_repeated_value_3(trees_repeated_value):
    do_test_repeated_value(trees_repeated_value, "tree_3", False)

def test_repeated_value_4(trees_repeated_value):
    do_test_repeated_value(trees_repeated_value, "tree_4", False)

def test_repeated_value_5(trees_repeated_value):
    do_test_repeated_value(trees_repeated_value, "tree_5", True)

# # #
#
# TEST TREES
#
# # #


@pytest.fixture(scope="session")
def trees_min_depth_leaf():
    """
    Fixture for loading the trees for min_depth_leaf
    """
    return get_trees()

@pytest.fixture(scope="session")
def trees_repeated_value():
    """
    Fixture for loading the trees for repeated_value
    """
    return get_trees()

def get_trees():
    trees = util.load_trees("sample_trees.json")
    original_trees = util.load_trees("sample_trees.json")
    return trees, original_trees