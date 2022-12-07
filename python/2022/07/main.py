import time


class File:
    name: str = None
    size: int = None
    parent: 'Tree' = None

    def __init__(self, name: str, size: int, parent: 'Tree' = None):
        self.name = name
        self.size = size
        self.parent = parent


class Tree:
    parent: 'Tree' = None
    name: str = None

    def __init__(self, name: str, parent: 'Tree' = None):
        self.name = name
        self.parent = parent
        self.children = []

    @property
    def directories(self):
        directories = []
        for child in self.children:
            if isinstance(child, Tree):
                directories.append(child)
                directories.extend(child.directories)
        return directories

    def add_file(self, name: str, size: int):
        file = File(name, size, parent=self)
        self.children.append(file)
        return file

    def remove_file(self, name: str):
        for child in self.children:
            if child.name == name:
                self.children.remove(child)
                return child
        return None

    def add_directory(self, name: str):
        # if its already self, return it
        if name == self.name:
            return self

        # if directory already exists, return it
        for child in self.children:
            if isinstance(child, Tree) and child.name == name:
                return child

        # otherwise, create it
        subtree = Tree(name=name, parent=self)
        self.children.append(subtree)
        return subtree

    def size(self):
        size = 0
        size_map = {
            File: lambda x: x.size,
            Tree: lambda x: x.size(),
        }
        for child in self.children:
            size += size_map[type(child)](child)
        return size


def ch_dir(tree, name):
    if name == '..':
        return tree.parent
    return tree.add_directory(name=name)

def parse_input(inputs, root):
    current = root
    current.parent = root
    for line in inputs.splitlines():
        args = line.split()
        # process command
        match args:
            # process command, e.g. cd .., cd a, ls
            case ['$', 'cd', subdir]:
                current = ch_dir(tree=current, name=subdir)
            case ['$', 'ls']:
                continue
            case ['dir', subdir]:
                current.add_directory(name=subdir)
            case _:
                current.add_file(name=args[1], size=int(args[0]))
    return root


def part_one(inputs):
    root = Tree(name='/')
    tree = parse_input(inputs, root)
    # find all directories with size <= 100000
    directories = [d.size() for d in tree.directories if d.size() <= 100000]
    return sum(directories)


def part_two(inputs):
    s_total = 70_000_000 # total volume space
    s_required = 30_000_000 # total free volume space required
    root = Tree(name='/')
    tree = parse_input(inputs, root)
    # find all directories with size >= required_free_size
    s_need = s_required - (s_total - root.size()) # minimum space needed to free
    directories = sorted([d.size() for d in tree.directories if d.size() >= s_need])
    return directories[0]

def main():
    with open('input.txt', 'r', encoding="utf-8") as fp:
        inputs = fp.read()
        one = part_one(inputs=inputs)
        two = part_two(inputs=inputs)
        print(one)
        print(two)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    tot = end - start
    print(f'Completed in {tot:.6f} seconds')
