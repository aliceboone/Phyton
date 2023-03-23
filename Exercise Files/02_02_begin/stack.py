# """
# Python Data Structures - A Game-Based Approach
# Stack class
# Robin Andrews - https://compucademy.net/
# """
#
#
# class Stack:
#     def __init__(self): # init call de constructor
#         self.items = [] # the items property of the stack
#
#     def is_empty(self):
#         # return len(self.items) == 0
#         return not self.items
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#     def __str__(self):
#         return str(self.items)
#
# if __name__ == "__main__":
#     s = Stack()
#     print(s)
#     print(s.is_empty())
#     s.push(3)
#     print(s)
#     s.push(7)
#     s.push(5)
#     print(s)
#     print(s.pop())
#     print(s)
#     print(s.peek())
#     print(s.size())
#
#
#
# s = []
# s.append(1)
# s.append(2)
# s.append(3)
# print(s)
# s.pop()
# print(s)
# s.append(7)
# print(s)

# from collections import deque
# stack = deque()
# stack.append(4)
#
# print(stack)
# stack.pop()
# print(stack)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)





