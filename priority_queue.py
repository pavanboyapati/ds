class PriorityQueue:
    def __init__(self):
        self.__list = []

    def dequeue(self):
        if self.isEmpty():
            raise IndexError
        return self.__list.pop(0)

    def enqueue(self, item):
        if self.isEmpty():
            self.__list.append(item)
            return
        for i in range(len(self.__list)-1, -1, -1):
            if self.__list[i] < item:
                self.__list.insert(i+1, item)
                return
        self.__list.insert(0, item)

    def isEmpty(self):
        return len(self.__list) == 0

    def peek(self):
        return self.__list[0]

    def __str__(self):
        return str(self.__list)
