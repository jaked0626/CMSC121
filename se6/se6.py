from tree import Tree


def sum_cubes(n):
    """
    Recursively calculates the sum of the first n
    positive cubes.

    Input:
        n: positive integer.
    
    Returns: (integer) the value of the sum
        1^3 + 2^3 + ... + n^3
    
    This function may not use any loops or list
    comprehensions.
    """

    pass


def sublists(lst):
    """
    Computes all sublists of the input list.

    Input:
        lst: list of values
    
    Returns: (list of list of values) list of all
        sublists of lst.
    """

    pass


def min_depth_leaf(tree):
    """
    Computes the minimum depth of a leaf in the tree
    (length of shortest path from the root to a leaf).

    Input:
        tree: a Tree instance.
    
    Returns: (integer) the minimum depth of of a leaf
        in tree.
    """

    pass


def repeated_value(tree):
    """
    Determines whether there is a node in the input
    tree that has an ancestor with the same value.

    Input:
        tree: a Tree instance.
    
    Returns: a boolean indicating whether there is a 
    node in the tree that has an ancestor with the 
    same value.
    """
    
    pass


def repeated_value_r(tree, ancestor_values):
    """
    Helper function for repeated_value. Takes in a tree
    which may be a subtree of the original tree of
    interest, and determines if there is a node in the 
    input tree that has an ancestor in the original tree
    with the same value.

    Inputs:
        tree: a Tree instance, which may be a subtree of
            of the original tree.
        ancestor_values: the set of values of nodes in
            the original tree that are ancestors of the
            input tree.
    
    Returns: a boolean indicating whether there is a node
        in the input tree that has an ancestor in the
        original tree with the same value.
    """
    
    pass
