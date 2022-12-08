# Read the input and build a tree data structure
# / - root
# $ - instruction
#   - cd [.., dirname]
#   - ls
#       - dir dir_name
#       - file_size file_name
# On cd traverse the tree - either up or down to a node
# On ls add nodes to the tree and update the directory sizes all the way up to the root.
# Finally traverse down the tree from root and find dir sizes > 10K


class Node:
    is_dir = False
    size = 0
    parent = None

    def __init__(self, is_dir, name, size, parent):
        self.is_dir = is_dir
        self.size = size
        self.name = name
        self.children = []
        self.parent = parent


def handle_ls(current_node: Node, ls_output: list):
    # print("ls output", ls_output)
    if current_node is None:
        raise Exception("Cannot ls into when node is None")

    for output in ls_output:
        if output[0].startswith("dir"):
            new_node = Node(True, output[1], 0, current_node)
        else:
            new_node = Node(False, output[1], int(output[0]), current_node)

        current_node.children.append(new_node)


def handle_cd(current_node: Node, new_dir: str) -> Node:
    # print("change dir: ", new_dir)
    if new_dir == "..":
        # traverse up a node
        return current_node.parent
    else:
        # traverse down a node
        for i, child in enumerate(current_node.children):
            if child.name == new_dir:
                return current_node.children[i]


def build_file_system():
    output = []
    current_node = None
    root_node = None
    lsoutput = False
    with open("puzzle13_input") as f:
        for line in f:
            input = line.strip()
            command = input.split()

            if input.startswith("$"):
                if lsoutput:
                    handle_ls(current_node, output)
                    lsoutput = False
                    output.clear()
                if command[1] == "cd":
                    # handle special case of root
                    if current_node is None:
                        current_node = Node(True, "/", 0, None)
                        root_node = current_node
                    else:
                        current_node = handle_cd(current_node, command[2])
                if command[1] == "ls":
                    lsoutput = True
            else:
                lsoutput = True
                output.append(command)

    handle_ls(current_node, output)
    return root_node


def dfs(node: Node) -> int:
    if node.is_dir:
        for child in node.children:
            node.size += dfs(child)

    return node.size


def compare_size(size: int, wanted: int, condition: str) -> bool:
    if condition == "<=":
        return size <= wanted
    if condition == ">=":
        return size >= wanted


def bfs(node: Node, wanted: int, comp: str) -> tuple:
    queue = []
    queue.append(node)
    visited = set()
    visited.add(node)
    total = 0
    wanted_list = []
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr.is_dir and compare_size(curr.size, wanted, comp):
            total += curr.size
            wanted_list.append(curr.size)

        for child in curr.children:
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return total, wanted_list


def main():
    root = build_file_system()
    # calculate file sizes
    dfs(root)

    total_sum, wanted_list = bfs(root, wanted=100000, comp="<=")
    print("total: ", total_sum)

    print("unused space:", 70000000 - root.size)
    space_needed = 30000000 - (70000000 - root.size)
    print("space needed:", space_needed)
    total_sum, wanted_list = bfs(root, wanted=space_needed, comp=">=")
    print("directory to be evicted:", min(wanted_list))


if __name__ == "__main__":
    main()
