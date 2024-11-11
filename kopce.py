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
        if ij2k(i, j) <= beap[-1]:
            i = i + 1
            k = ij2k(i, j)
            continue
        j = j - 1
        k = ij2k(i, j)
    if j == 0:
        return -1
    return k

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
h.print_all_preorder(h)










