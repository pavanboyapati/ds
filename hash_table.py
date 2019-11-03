from linked_list import LinkedList
from functools import reduce


class HashTable:
    class Entry:
        def __init__(self, k, v):
            self.key = k
            self.value = v

    def __init__(self, size=10):
        self.__list = []
        for i in range(0, size):
            self.__list.append(LinkedList())

    def __str__(self):
        return str(self.__list)

    def put(self, k, v):
        index = self.__hash(k)
        ll = self.__list[index]
        e = self.Entry(k, v)

        current_item = ll.head

        while current_item:
            if current_item.value.key == k:
                current_item.value.value = v
            current_item = current_item.next

        ll.add(e)

    def get(self, k):
        index = self.__hash(k)

        ll = self.__list[index]

        current_item = ll.head

        while current_item:
            if current_item.value.key == k:
                return current_item.value.value
            current_item = current_item.next
        return

    def remove(self, k):
        index = self.__hash(k)
        ll = self.__list[index]

        current_item = ll.head

        while current_item:
            if current_item.value.key == k:
                return ll.remove(id(current_item.value))
            current_item = current_item.next
        return False

    def contains(self, k):
        index = self.__hash(k)
        ll = self.__list[index]
        current_item = ll.head

        while current_item:
            if current_item.value.key == k:
                return True
            current_item = current_item.next
        return False

    def __hash(self, key):
        if type(key) in [int, float]:
            return abs(int(key)) % len(self.__list)
        if type(key) is str:
            l = [ord(c) for c in key]
            s = reduce(lambda a, b: a+b, l)
            return abs(int(s)) % len(self.__list)
