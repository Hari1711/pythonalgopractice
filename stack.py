class StackOverflowError(BaseException):
    pass
class StackUnderflowError(BaseException):
    pass

class Stack:
    def __init__(self,stack_size):
        self.stack_size=stack_size
        self.stack=[]
    def __bool__(self):
        return bool(self.stack)
    def __str__(self):
        return str(self.stack)
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return not bool(self.stack)
    def is_full(self):
        return self.size()==self.stack_size
    def push(self,data):
        if self.is_full():
            raise StackOverflowError
        else:
            self.stack.append(data)
    def pop(self):
        if self.is_empty():
            raise StackUnderflowError
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise stackunderflow
        else:
            return self.stack[-1]
    def __contains__(self,item):
        return item in stack
"""
parentheses checker 
"""
def parentheses_checker(expr):
     stack=Stack(100)
     bracket_pairs={'(':')','{':'}','[':']'}
     for bracket in expr:
        if bracket in bracket_pairs:
            stack.push(bracket)
        elif bracket in [')','}',']']:
            if stack.is_empty() or bracket_pairs[stack.pop()]!=bracket:
                return False
     return stack.is_empty()

print(parentheses_checker("({[})"))
