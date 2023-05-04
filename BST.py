# self-balancing binary search tree
# TODO self-balancing function

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return "val: %s\nparent: %s\nleft child: %s\nright child: %s" % (self.data, self.parent, self.left, self.right)


class BST:
    def __init__(self, arr):
        self.root = None

        for val in arr:
            self.insert(val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            node = self.root
            flag = True
            while flag:
                if node.data > val:
                    if node.left is None:
                        node.left = Node(val, node)
                        flag = False
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(val, node)
                        flag = False
                    else:
                        node = node.right

    def find(self, val):
        if self.root is None:
            return False

        else:
            node = self.root

            while True:
                if node.data > val:
                    if node.left is None:
                        return False
                    else:
                        node = node.left
                elif node.data < val:
                    if node.right is None:
                        return False
                    else:
                        node = node.right
                else:
                    return node

    def delete(self, val):
        node = self.find(val)
        if node == False:
            raise KeyError(f"{val} does not exist in the Array")

        # ノードの子の数に応じて処理を変える
        if node.left and node.right:
            r_min = self.bst_min(node.right)
            target = r_min
            r_min.parent = node.parent
        elif node.left:
            target = node.left
            node.left.parent = node.parent
        elif node.right:
            target = node.right
            node.right.parent = node.parent
        else:
            target = None

        # 変更したノードの親との関係性も変更する必要がある
        if node.parent.left and node.parent.left.val == val:
            node.parent.left = target
        else:
            node.parent.right = target

        print("parent: %s" % node.parent.right)

    def bst_min(self, node):
        if node.left is None:
            return node
        else:
            return self.bst_min(node.left)
            # 再帰で行きついた先の値を返したいときはreturn のあとに再帰関数を書く。traversalのときと用法が異なるので注意。

    def bst_max(self, node):
        if node.right is None:
            return node
        else:
            return self.bst_max(node.right)

    def get_root(self):
        return self.root

    def get_max(self):
        return self.bst_max(self.get_root)

    def get_min(self):
        return self.bst_min(self.get_root)

    def inoder_traverse(self, node):
        if node is not None:
            self.inoder_traverse(node.left)
            print(node.data)
            self.inoder_traverse(node.right)

    def get_inorder_traverse(self):
        self.inoder_traverse(self.root)


if __name__ == "__main__":
    arr = [8, 4, 6, 10, 13, 14]
    bst = BST(arr)
    bst.insert(9)
    print(bst.find(7))
    bst.delete(6)
    bst.get_inorder_traverse()
