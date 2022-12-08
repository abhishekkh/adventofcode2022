import pytest

from adventofcode2022 import puzzle13


def test_build_tree():
    file_name = "sample_input_13.txt"
    root = puzzle13.build_file_system(file_name=file_name)

    assert root.size == 0
    assert root.name == "/"

    assert root.children[0].children[0].name == "fc"
    assert root.children[1].children[0].name == "fd"

def test_root_size():
    file_name = "sample_input_13.txt"
    root = puzzle13.build_file_system(file_name=file_name)

    assert puzzle13.dfs(root) == 1000
