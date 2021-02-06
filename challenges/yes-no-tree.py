class Node:

    def __init__(self, question, answer):

        self.left = None
        self.right = None
        self.question = question
        self.answer = answer

    def insert(self, question, answer):
        # Compare the new value with the parent node
        if self.question:
            if answer == "Y":
                if self.left is None:
                    self.left = Node(question, answer)
                else:
                    self.left.insert(question, answer)
            elif question == "N":
                if self.right is None:
                    self.right = Node(question, answer)
                else:
                    self.right.insert(question, answer)
        else:
            self.question = question
            self.answer = answer

        # Print the tree

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.question, self.answer),
        if self.right:
            self.right.printTree()

