class EmptyQueueException(Exception):
    def __str__(self):
        return "Queue is empty"


class Queue(object):

    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(self.__list)  # .__str__()

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        if len(self.__list) == 0:
            raise EmptyQueueException()
        self.__list.pop(0)

    def peek(self):
        if len(self.__list) == 0:
            raise EmptyQueueException()
        return self.__list[0]
