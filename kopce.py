import math
# KOPIEC - DRZEWO BINARNE ZUPEŁNE, W KTÓRYM RODZIC MA WIĘKSZĄ WARTOŚĆ NIŻ SYNOWIE

# wstaw wartość v do kopca
def up_heap(heap, v):
    heap.append(v)
    current_ind = len(heap) - 1
    parent_ind = (len(heap) - 1) // 2
    while heap[parent_ind] < heap[current_ind] and parent_ind >= 0:
        heap[parent_ind], heap[current_ind] = heap[current_ind], heap[parent_ind]
        current_ind = parent_ind
        parent_ind = (parent_ind - 1) // 2
    return heap

# usuń maksymalny element z kopca
def down_heap(heap):
    heap[0] = heap.pop()
    current_ind = 0
    leftchild_ind = 2 * current_ind + 1
    rightchild_ind = 2 * current_ind + 2
    while leftchild_ind < len(heap) and rightchild_ind < len(heap) and (heap[current_ind] < heap[leftchild_ind] or heap[current_ind] < heap[rightchild_ind]):
        if heap[leftchild_ind] > heap[rightchild_ind]:
            heap[current_ind], heap[leftchild_ind] = heap[leftchild_ind], heap[current_ind]
            current_ind = leftchild_ind
        else:
            heap[current_ind], heap[rightchild_ind] = heap[rightchild_ind], heap[current_ind]
            current_ind = rightchild_ind
        leftchild_ind = 2 * current_ind + 1
        rightchild_ind = 2 * current_ind + 2
    return heap

heap = [18,13,16,8,10,15,13,7,2]
#print(down_heap(heap))

# DWUKOPIEC - TAKI KOPIEC TYLKO ZE NA n-TYM POZIOMIE JEST N WEZLOW
beap = [30, 20, 10, 4, 5, 6, 2, 1]

# zwraca ponumerowany wezel ze wzgledu na (i,j)
def ij2k(i, j):
    return (i // 2) * (i - 1) + j

# zwraca pare (i,j) ze wzgledu na numeracje wezla
def k2ij(k):
    k -= 1
    i = math.floor((math.sqrt(8 * k + 1) - 1) / 2) + 1
    start_index = i * (i - 1) // 2
    j = k - start_index + 1
    return (i, j)

# szuka wezla o wartosci v. jesli jest, to zwraca jego k, w przeciwnym wypadku zwraca -1
def search(v, beap):
    (i, j) = k2ij(len(beap))
    if i != j:
        i = i - 1
        j = i
    k = ij2k(i, j)
    while beap[k - 1] != v and j > 0:
        if v > beap[k - 1]:
            i = i - 1
            j = j - 1
            k = ij2k(i, j)
            continue
        if len(beap) >= ij2k(i + 1, j):
            i = i + 1
            k = ij2k(i, j)
            continue
        j = j - 1
        k = ij2k(i, j)
    if j == 0:
        return -1
    return k

print(search(1, beap))

# kopiec skośny - dowolne drzewo binarne z własnościami kopca
class Node:
    root = None
    def __init__(self, val, left=None, right=None, npl=None):
        self.val = val
        self.left = left
        self.right = right
        self.npl = npl
        if self.root is None:
            self.root = self

    # kopiec lewostronny - wartość NPL (odleglosc od najbliższego None) po lewej >= po prawej
    def setNPL(self, root):
        if root is None:
            return -1
        npl_left = self.setNPL(root.left)
        npl_right = self.setNPL(root.right)
        npl = min(npl_left, npl_right) + 1
        root.npl = npl
        return npl

    def print_all_preorder(self, root):
        if root is None:
            return
        print(root.val, root.npl)
        self.print_all_preorder(root.left)
        self.print_all_preorder(root.right)

    def union(self, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        if p1.val < p2.val:
            p1, p2 = p2, p1
        p1.right = self.union(p1.right, p2)
        # kopiec skośny: p1.left, p1.right = p1.right, p1.left
        # kopiec lewostronny:
        # if p1.left.npl < p1.right.npl:
        #   p1.left, p1.right = p1.right, p1.left
        #   p1.npl = min(p1.left.npl, p1.right.npl) + 1
        return p1
    # zlozonosc zamortyzowana - zlozonosc pesymistyczna w ciagu n operacji na jedna operacje

# tworze sb kopca skosnego i ustawiam na niego npl
h = Node(10)
h.right = Node(7)
h.left = Node(8)
h.left.left = Node(3)
h.left.right = Node(2)
h.right.right = Node(5)
h.right.left = Node(6)
h.left.right.left = Node(1)
h.setNPL(h)
# h.print_all_preorder(h)


# drzewa dwumianowe, kolejki dwumianowe, kopce fibonacciego

# drzewo dwumianowe - nwm dziwne jakies, prev i next to wskazniki na poprzednie
# i nastepne rodzenstwo, child to wskaznik na najbardziej lewe dziecko
# warto dodac, ze prev pierwszego dziecka to ostatnie dziecko
class Node:
    root = None
    def __init__(self, val, child=None, h=None, prev=None, next=None, marked=False):
        self.val = val
        self.child = child
        self.h = h
        self.prev = prev
        self.next = next
        self.marked = marked
        if self.root is None:
            self.root = self

    def print_all(self, root):
        if root is None:
            return
        print(root.val)
        p = root.child
        while p is not None:
            self.print_all(p)
            p = p.next

    def missing_index(self, root):
        if root.marked == False:
            return -1
        hArray = [False] * h
        p = root.child
        while p is not None:
            hArray[p.h] = True
            p = p.next
        for i in range(root.h):
            if not hArray[i]:
                return i

    # t2 staje sie najbardziej prawym dzieckiem t1
    def margeTrees(self, t1, t2):
        if t1.val < t2.val:
            t1, t2 = t2, t1
        if t1.child is not None:
            t1.child.prev.next = t2
            t2.prev = t1.child.prev
            t1.child.prev = t2
        else:
            t1.child = t2
            t1.h = t1.h + 1
        return t1

# kolejka dwumianowa - kolekcja kopcow dwumianowych w kolejnosci posortowanej rosnaco

class Node:
    root = None
    def __init__(self, val, child=None, h=None, prev=None, next=None, marked=False):
        self.val = val
        self.child = child
        self.h = h
        self.prev = prev
        self.next = next
        self.marked = marked
        if self.root is None:
            self.root = self
    def addToEnd(self, p, t):
        if p is not None:
            plast = p.prev
            plast.next = t
            t.prev = plast
            p.prev = t
            return p
        else:
            return t
    def extract(self, p):
        if p is None:
            return (None, None)
        t = p
        p = p.next
        if p is None:
            return (t, None)
        t.next = None
        p.prev = t.prev
        t.prev = t
        return (t, p)
    def correctAndAddToEnd(self, p, t):
        # marked pokazuje ilu drzew brakuje, w tym zadaniu przyjmuje wartosc 0, 1 lub 2
        if t.marked == 0:
            return self.addToEnd(p, t)
        if t.marked == 1:
            if t.child.prev.h == t.h - 2:
                t.h = t.h - 1
                t.marked = 0
            return self.addToEnd(p, t)
        if t.marked == 2:
            if t.child.prev.h == t.h - 3:
                t.h = t.h - 2
                t.marked = 0
                return self.addToEnd(p, t)
            if t.child.prev.h == t.h - 2:
                t.h = t.h - 1
                t.marked = 0
                return self.addToEnd(p, t)
            ptr = t.child
            while ptr is not None:
                (t1, ptr) = self.extract(ptr)
                p = self.addToEnd(p, t1)
            t.h, t.marked, t.child = 0, 0, None
            return self.addToEnd(p, t)




