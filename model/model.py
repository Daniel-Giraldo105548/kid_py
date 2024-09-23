from pydantic import BaseModel
class Kid(BaseModel):
    id:str
    name:str
    age:int
class NodeDE:

    def __init__(self, kid: Kid):
        self.__data = kid
        self.__next = None
        self.__previous = None

    def get_data(self):
        return self.__data

    def set_data(self, data:Kid):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def get_previous(self):
        return self.__previous

    def set_previous(self, node):
        self.__previous = node


class ListDE:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_head(self):
        return self.__head

    def set_head(self, node):
        self.__head = node

    def get_size(self):
        return self.__size

    def set_size(self, size:int):
        self.__size = size


    def add(self, data:Kid):
        if self.__head == None:
            self.__head = NodeDE(data)