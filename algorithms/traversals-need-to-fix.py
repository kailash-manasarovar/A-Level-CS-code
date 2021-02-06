# tree = [[1, '+', 2],
#         [3, '*', 4],
#         [5, '/', 6],
#         [-1, 'a', -1],
#         [-1, 'b', -1],
#         [-1, 'c', -1],
#         [-1, 'd', -1]]
#
#
# def inorderTraverse(p):
#     if tree[p].left != -1:
#         inorderTraverse(tree[p].left)
#     print(tree[p].data)
#     if tree[p].right != -1:
#         inorderTraverse(tree[p].right)
#
#
# inorderTraverse(0)
# no left or right


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()



    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        return (self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)) if root else []

    # post order
    # bottom left up -> bottom right up
    def postorderTraversal(root):
        if root:
            # recursion on left
            root.postorderTraversal(root.left)
            # recursion on right child
            root.postorderTraversal(root.right)
            # now print the data of node
            print(root.data)
        else:
            pass


def postorder(tree):
    data = []

    def recurse(node):
        if not node:
            return
        recurse(node.left)
        recurse(node.right)
        data.append(node.data)

    recurse(tree)
    return data


root = Node('C')
root.insert('D')
root.insert('B')
root.insert('A')
root.insert('F')
root.insert('G')
print(root.PrintTree())
#root.postorderTraversal()
postorder(root)