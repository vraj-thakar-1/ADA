# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def push(self, e):
#         self.items.append(e)
#
#     def pop(self):
#         head = self.items[0]
#         self.items = self.items[1:]
#         return head
#
#
# q = Queue()
# q.push(23)
# q.push(23)
# q.push(234)
# print(q.pop())


class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items=[+e]+self.items

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head


q = Stack()
q.push(23)
q.push(2)
q.push(234)
print(q.items)
print(q.pop())