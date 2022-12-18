# Tree

import time
from random import randint


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            node = self.root
            while node:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    node = node.right

    def remove(self, data):
        if self.root is None:
            return
        if self.root.data == data:
            self.root = None
            return
        node = self.root
        while node:
            if data < node.data:
                if node.left.data == data:
                    node.left = None
                    break
                node = node.left
            else:
                if node.right.data == data:
                    node.right = None
                    break
                node = node.right

    def search(self, data):
        node = self.root
        while node:
            if data == node.data:
                return True
            node = node.left if data < node.data else node.right
        return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.root.data)


if __name__ == '__main__':

    tree = Tree()

    start = time.time()
    for _ in range(100000):
        tree.add(randint(0, 100))
    end = time.time()
    print(end - start)

    start = time.time()
    liste = [randint(0, 100) for _ in range(100000)]
    end = time.time()
    print(end - start)

    # time test


    start = time.time()
    print(tree.search(50))
    end = time.time()
    print(end - start)

    start = time.time()
    print(50 in liste)
    end = time.time()
    print(end - start)