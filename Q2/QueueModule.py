class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):    #從最左邊加入
        self.items.insert(0, item)

    def dequeue(self):  #從最右邊彈出
        return self.items.pop()

    def size(self):
        return len(self.items)
