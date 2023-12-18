class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            head = self.top
            while head.next:
                head = head.next
            head.next = obj

    def pop_back(self):
        head = self.top
        while head.next.next:
            head = head.next
        head.next = None

    def __do(self, other):
        if not isinstance(other, (StackObj, list)):
            raise TypeError("Неверный тип операнда для операции")

        other = (other,)
        if isinstance(other, list):
            other = map(lambda x: StackObj(x), other)

        for i in other:
            self.push_back(i)

        return self

    def __add__(self, other):
        return self.__do(other)

    def __mul__(self, other):
        return self.__do(other)
