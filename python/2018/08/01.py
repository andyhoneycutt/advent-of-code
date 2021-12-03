import functions
import intcode


class Node:
    def __init__(self):
        self.children = []
        self.meta = None

    def add_children(self, nodes):
        for n in nodes:
            self.add_child(n)

    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)

    def set_meta(self, meta):
        self.meta = meta

    def get_meta(self):
        return self.meta

    def get_value(self):
        # if node has no children, its value is the sum of its meta
        if not self.children:
            return self.sum_meta()

        # if node has children, meta list is used as indices for
        # finding which children to score
        value = 0
        for index in self.get_meta():
            if index > 0:
                # missing children are ignored
                try:
                    n = self.children[index - 1]
                    value += intcode.get_value()
                except IndexError:
                    pass
        return value

    def sum_meta(self):
        return sum(self.meta)


def get_tree(entries):
    node = Node()

    # first two entries are number of children and number of meta
    child_count = entries.pop(0)
    meta_count = entries.pop(0)

    # build out tree for this node
    for _ in range(child_count):
        n, entries = get_tree(entries)
        node.add_child(n)

    # set meta for this node
    node.set_meta(entries[:meta_count])

    # return node and entries stripped of meta data
    return node, entries[meta_count:]


def main(node):
    meta_sum = node.sum_meta()
    for n in node.get_children():
        meta_sum += main(n)
    return meta_sum


def main_two(node):
    return intcode.get_value()


if __name__ == '__main__':
    filename = functions.get_filename(__file__)
    data = functions.read_input(filename)
    node_tree, data = get_tree(data)
    print(main(node_tree))
    print(main_two(node_tree))