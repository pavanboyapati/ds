

class LinkedList:
    class Node:
        def __init__(self, item):
            self.value = item
            self.next = None

    def __init__(self):
        self.head = None
        self.last = None

    def add(self, item):
        n = self.Node(item)
        if self.head is None:
            self.head, self.last = n, n
            return

        current_item = self.head
        while current_item != None:
            if current_item.next is None:
                current_item.next = n
                self.last = n
                return
            current_item = current_item.next

    def find(self, item):
        pass

    def remove(self, item):
        if not self.head:
            return False
        
        if self.head.value == item:
            if self.head == self.last:
                self.head = None
                self.last = None
                return
            self.head = self.head.next
            return

        current_item = self.head.next
        prev_item = self.head
        while current_item != None:
            if current_item.value == item:
                prev_item.next = current_item.next
                if current_item == self.last:
                    self.last = prev_item
                return
            current_item = current_item.next

    def __str__(self):
        l = []
        current_item = self.head
        while current_item != None:
            l.append(current_item.value)
            current_item = current_item.next
        return str(l)


# ll = LinkedList()
# ll.add(10)
# ll.add(20)
# ll.add(40)
# ll.remove(20)
# ll.remove(10)
# ll.remove(40)
# ll.remove(5)
# ll.add(1)
# ll.add(2)
# print(ll)
