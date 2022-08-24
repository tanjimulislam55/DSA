from typing import List


class TreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def insert(self, data: int) -> None:
        temp: TreeNode = self.root

        while True:
            if data < temp.data:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = TreeNode(data)
                    break
            else:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = TreeNode(data)
                    break

    def insert_using_stack(self, data: int):
        stack = List[self.root]

        while stack:
            item: TreeNode = stack.pop()
            if item.data > data:
                pass
            else:
                pass

    def search(self, data: int) -> None:
        pass

    def inorder_traversal_using_recursion(self, root: TreeNode) -> None:
        if root is None:
            return
        if root.left:
            self.inorder_traversal_using_recursion(root.left)
        print(root.data)
        if root.right:
            self.inorder_traversal_using_recursion(root.right)
        return

    def preorder_traversal_using_recursion(self, root: TreeNode) -> None:
        if root is None:
            return
        print(root.data)
        if root.left:
            self.preorder_traversal_using_recursion(root.left)
        if root.right:
            self.preorder_traversal_using_recursion(root.right)
        return

    def inorder_traversal_using_stack(self, root: TreeNode) -> None:
        stack, temp = [], root
        while stack or temp:
            while temp:
                stack.append(temp)
                temp = temp.left
            k: TreeNode = stack.pop()
            print(k.data)
            temp: TreeNode = k.right

    def update(self, data: int) -> None:
        pass

    def delete(self, data: int) -> None:
        pass


# [100, 7, 3, 50, 99, 101]
t1 = Tree(TreeNode(100))
t1.insert(7)
t1.insert(3)
t1.insert(50)
t1.insert(99)
t1.insert(101)
# print(t1.inorder_traversal_using_recursion(t1.root))
# print(t1.inorder_traversal_using_stack(t1.root))
print(t1.preorder_traversal_using_recursion(t1.root))
