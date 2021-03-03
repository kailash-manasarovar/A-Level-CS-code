
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)

    # in order
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)


r = Node(27)
r.insert(r, Node(14))
r.insert(r, Node(35))
r.insert(r, Node(10))
r.insert(r, Node(19))
r.insert(r, Node(31))
r.insert(r, Node(42))





# ## SEARCH
def search(root, key):
    # Recursive base case: root is null or key is present at root
    if root is None or root.data == key:
        return root

    # Key is greater than root's key
    if root.data < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

print(search(r, 31))


# ## TRAVERSAL

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print(root.data)
    in_order_print(root.right)

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.left)
    pre_order_print(root.right)

def post_order_print(root):
    if not root:
        return
    post_order_print(root.left)
    post_order_print(root.right)
    print(root.data)

#
print("in order:")
in_order_print(r)

print("pre order")
pre_order_print(r)

print("post order")
post_order_print(r)