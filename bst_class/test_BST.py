import pytest
from BSTTree import Tree
from BSTNode import Node


@pytest.fixture
def make_tree():
    my_tree = Tree()
    keys = [12, 2, 9, 5, 18, 15, 19, 13, 17]

    for key in keys:
        my_tree.put(key=key, val=key*key)
    
    yield

    del my_tree

def test_creation_of_tree(make_tree):
    pass
