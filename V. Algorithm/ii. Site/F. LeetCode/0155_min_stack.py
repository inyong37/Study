class MinStack:
    def __init__(self):
        self.__stack = list()

    def push(self, val: int) -> None:
        if self.__stack:
            self.__stack.append((val, min(val, self.__stack[-1][1])))
        else:
            self.__stack.append((val, val))

    def pop(self) -> None:
        if self.__stack:
            return self.__stack.pop()
    
    def top(self) -> int:
        if self.__stack:
            return self.__stack[-1][0]

    def getMin(self) -> int:
        return self.__stack[-1][1]
