class Stack:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError
        return self.__list.pop(-1)

    def peek(self):
        if self.isEmpty():
            raise IndexError
        return self.__list[-1]

    def isEmpty(self):
        return len(self.__list) == 0
