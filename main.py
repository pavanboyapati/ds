from priority_queue import PriorityQueue as Queue
from hash_table import HashTable

if __name__ == "__main__":
    # l = (1, 2)
    # l[0] = 2
    # l[1] = 3
    # print(l)
    # q = Queue()
    # q.enqueue(10)
    # q.enqueue(2)
    # q.enqueue(30)
    # q.enqueue(15)
    # print(q)
    # q.dequeue()
    # q.dequeue()
    # q.dequeue()
    # q.enqueue(20)
    # print(q.peek())
    # q.enqueue(25)
    # q.enqueue(40)
    # q.enqueue(10)
    # print(q)

    # hash table test
    ht = HashTable(size=5)
    ht.put(1, 'pavan')
    ht.put(406, 'kumar')
    ht.put(506, 'lav')
    ht.put(506, 'kus')
    ht.put('pavan', 5)
    ht.put('pavan', 'kumar')
    ht.remove('pavan')
    print(ht.get(506))
