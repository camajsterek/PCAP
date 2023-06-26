# Defining classes for a FIFO Queue

class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.que = []

    def put(self, elem):
        self.que.append(elem)

    def get(self):
        if len(self.que) > 0:
            elem = self.que[0]
            del self.que[0]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.que) > 0:
            return False
        else:
            return True


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
