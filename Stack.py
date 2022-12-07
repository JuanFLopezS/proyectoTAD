class Stack:
    def __init__(self, list):
        self.stack = list
        self.head = self.stack[len(self.stack) - 1]

    def add(self, card):
        self.head = card
        self.stack.append(card)

    def delete(self):
        if len(self.stack) == 0:
            return
        elif len(self.stack) == 1:
            self.stack.pop()
            self.head = None
        else:
            self.stack.pop()
            self.head = self.stack[len(self.stack) - 1]

    def winner(self, list: list):
        if self.stack == list:
            return True
        else:
            return False