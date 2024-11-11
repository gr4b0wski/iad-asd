class Node:
    root = None
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        if self.root is None:
            self.root = self
    # do przeszukiwania DFS
    def print_all_preorder(self, root):
        if root is None:
            return
        print(root.val)
        self.print_all_preorder(root.left)
        self.print_all_preorder(root.right)
    # dla drzew BST inorder wypisuje posortowane wartości
    def print_all_inorder(self, root):
        if root is None:
            return
        self.print_all_inorder(root.left)
        print(root.val)
        self.print_all_inorder(root.right)
    # do odwróconej notacji polskiej
    def print_all_postorder(self, root):
        if root is None:
            return
        self.print_all_postorder(root.left)
        self.print_all_postorder(root.right)
        print(root.val)
    # taki preorder tylko że od prawej
    def print_all_nonrecursive(self):
        s = []
        s.append(self.root)
        while len(s) != 0:
            p = s.pop()
            print(p.val)
            if p.left:
                s.append(p.left)
            if p.right:
                s.append(p.right)
    # wypisywanie poziomami (BFS)
    def print_all_by_breadth(self):
        q = []
        q.append(self.root)
        while len(q) != 0:
            p = q.pop(0)
            print(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

d = Node(3)
d.right = Node(7)
d.left = Node(8)
d.left.left = Node(4)
d.left.right = Node(5)
d.left.right.right = Node(1)
d.right.left = Node(2)
d.print_all_by_breadth()


