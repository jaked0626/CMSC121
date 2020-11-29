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
    if n == 1:
        return 1
    else:
        return n ** 3 + sum_cubes(n-1)




def sublists(lst):
    """
    Computes all sublists of the input list.

    Input:
        lst: list of values
    
    Returns: (list of list of values) list of all
        sublists of lst.
    """
    copy_lst = lst[:]
    if len(copy_lst) == 0:
        sublst = [[]]
        return sublst
    else:
        x = [copy_lst.pop(0)]
        sublst_minus_x = sublists(copy_lst)
        sublst = sublst_minus_x[:]
        
        for v_lst in sublst_minus_x:
            new_lst = x + v_lst
            sublst.append(new_lst)
            
        return sublst



def min_depth_leaf(tree):
    """
    Computes the minimum depth of a leaf in the tree
    (length of shortest path from the root to a leaf).

    Input:
        tree: a Tree instance.
    
    Returns: (integer) the minimum depth of of a leaf
        in tree.
    """
    if tree.num_children() == 0:
        return 0
    else: 
        lst = [min_depth_leaf(child) for child in tree.children] # returns minimum depth of each child.
        return min(lst) + 1




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
    boolean = False
    for child in tree.children:
        if repeated_value_r(child, set([tree.value])):
            boolean = True
            break
    return boolean


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
    if tree.value in ancestor_values:
        return True
    else:
        if tree.num_children() > 0:
            boolean = False
            new_ancestors = ancestor_values.copy()
            new_ancestors.add(tree.value)
            for child in tree.children:
                if repeated_value_r(child, new_ancestors):
                    boolean = True
                    break
            return boolean
        else: 
            return False
        

