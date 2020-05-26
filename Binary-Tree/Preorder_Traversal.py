class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class iterative_solution:
    def preorderTraversal(self, root: TreeNode):
        result, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right

        return result

class recursive_solution:
    def preorderTraversal(self, root: TreeNode):
        output = []
        self._temp_(root, output)
        return output

    def _temp_(self, root, output):
        if root is None:
            return
        output.append(root.val)
        self._temp_(root.left, output)
        self._temp_(root.right, output)

if __name__ == "__main__":
    Tree = TreeNode(1,
                    TreeNode(2,
                             TreeNode(5,
                                      None,
                                      None),
                             None),
                    TreeNode(3,
                             None,
                             TreeNode(4,
                                      None,
                                      None)))

    print(iterative_solution().preorderTraversal(Tree))
    # print(recursive_solution().preorderTraversal(Tree))
