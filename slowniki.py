# drzewa BST
class Node:
    root = None
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        if self.root is None:
            self.root = self
    # zwraca szukany element i rodzica szukanego elementu
    def search(self, v):
        p = self.root
        last = None
        while p is not None and p.key != v:
            if v < p.key:
                last = p
                p = p.left
            else:
                last = p
                p = p.right
        return (p, last)

    # wstaw element do drzewa BST
    def insert(self, v):
        p, last = self.search(v)
        if p is not None:
            return
        p = Node(v)
        if last is None:
            root = p
        else:
            if v < last.key:
                last.left = p
            else:
                last.right = p
        return

    # usun element z drzewa BST
    def delete(self, v):
        p, last = self.search(v)
        if p is None:
            return
        # lisc
        if p.left is None and p.right is None:
            # ...
            return
        # tylko 1 dziecko -> pChild
        if p.right is None or p.left is None:
            if p.right is None:
                pChild = p.left
            else:
                pChild = p.right
            if last is None:
                self.root = pChild
                return
            if p == last.left:
                last.left = pChild
            else:
                last.right = pChild
        # dwoje dzieci
        # ... za trudne xD

    # drzewo BST zrównoważone - takie modyfikacje drzew BST, które gwarantują,
    # że pesymistyczna złożność operacji search(v) jest logarytmiczna
    # np. drzewa AVL, drzewa czerwono-czarne

    # drzewo AVL- definiujemy dla każdego węzła BL (balans) który oznacza
    # wysokosc lewego poddrzewa - wysokosc prawego, musi byc w zbiorze {-1,0,1}






