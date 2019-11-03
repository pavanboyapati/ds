from stack import Stack


class QueueWithTwoStacks(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def __str__(self):
        l1 = self.s2.__str__()[1:len(
            self.s2.__str__())-1].split(", ")
        l1.reverse()
        l3 = list(map(int, l1))
        l2 = list(map(int,self.s1.__str__()[
            1:len(self.s1.__str__())-1].split(", ")))
        if l2[0] is '':
            l2 = []
        # print(l1[1:len(l1)-1])
        return f'{list(l3+l2)}'

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            raise Exception("Empty Queue")
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            raise Exception("Empty Queue")
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()
