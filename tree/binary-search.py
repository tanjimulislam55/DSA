class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def insert(self, data):
        temp: TreeNode = self.root

        while True:
            if temp.data > data:
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

    def search(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, data):
        pass
