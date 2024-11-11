import sys


class Node:
    head = None
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        if self.head is None:
            self.head = self
    def push_front(self, val):
        self.head = Node(val, self.head)
    def push_back(self, val):
        if self.head is None:
            self.push_front(val)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val, None)
    def pop_front(self):
        if self.head is not None:
            p = self.head
            self.head = p.next
    def pop_back(self):
        if self.head is None:
            return
        p = self.head
        while p.next.next is not None:
            p = p.next
        p.next = None
    def print_all(self):
        p = self.head
        while p is not None:
            print(p.val)
            p = p.next
        print("")
    def print_all_reversed(self, head):
        if head is None:
            return
        self.print_all_reversed(head.next)
        print(head.val)
    def del_max_element(self):
        if self.head is None:
            return
        p = self.head.next
        p_prev = self.head
        p_max = p
        p_max_prev = p_prev
        max_val = -sys.maxsize - 1
        while p is not None:
            if p.val > max_val:
                max_val = p.val
                p_max = p
                p_max_prev = p_prev
            p = p.next
            p_prev = p_prev.next
        if self.head.val > p_max.val:
            self.pop_front()
        else:
            p_max_prev.next = p_max.next
            p_max.next = None

    def insert_to_sorted_list(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        if val < self.head.val:
            self.head = Node(val, self.head)
            return
        p_prev = self.head
        p = self.head.next
        while p is not None:
            if val < p.val:
                p_prev.next = Node(val, p)
                return
            p = p.next
            p_prev = p_prev.next

    def del_value(self, val):
        if self.head is None:
            return
        if self.head.val == val:
            self.pop_front()
        p_prev = self.head
        p = self.head.next
        while p is not None:
            if p.val == val:
                p_prev.next = p.next
                p.next = None
            p = p.next
            p_prev = p_prev.next
    def del_duplicates(self):
        if self.head is None:
            return
        p = self.head
        while p.next is not None:
            r_prev = p
            r = p.next
            while r is not None:
                if p.val == r.val:
                    r_prev.next = r.next
                    r.next = None
                    r = r_prev.next
                else:
                    r = r.next
                    r_prev = r_prev.next
            p = p.next

    def merge_sorted(self, l1, l2):
        self.push_front(0)
        p = self.head
        while l1.head is not None and l2.head is not None:
            if l1.head.val < l2.head.val:
                p.next = l1.head
                l1.pop_front()
            else:
                p.next = l2.head
                l2.pop_front()
            p = p.next
        if l1.head is not None:
            p.next = l1.head
            l1.head = None
        if l2.head is not None:
            p.next = l2.head
            l2.head = None
        self.pop_front()


l1 = Node(1)
l1.push_back(5)
l1.push_back(7)
l2 = Node(2)
l2.push_back(3)
l2.push_back(4)
l2.push_back(8)
l2.push_back(9)
n = Node()
n.merge_sorted(l1, l2)
n.print_all()
