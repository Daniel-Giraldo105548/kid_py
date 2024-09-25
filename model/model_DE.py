from idlelib.sidebar import temp_enable_text_widget

from contoller.list_de_controller import addToStart
from model.model import Kid


class NodeDE:

    def __init__(self, kid: Kid):
        self.__data = kid
        self.__next = None
        self.__previous = None

    def get_data(self):
        return self.__data

    def set_data(self, data: Kid):
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

    def addDE(self, data:Kid):
        if self.__head == None:
            self.__head = NodeDE(data)
        else:
            temp = self.__head
            while temp.get_next() is not None:
                temp = temp.get_next()

            new_node = NodeDE(data)
            temp.set_next(new_node)
            new_node.set_previous(temp)

    def addToStart(self, data: Kid):
        if self.__head == None:
            self.__head = NodeDE(data)
        else:
            new_node = NodeDE(data)
            new_node.set_next(self.__head)
            self.__head.set_previous(new_node)
            self.__head = new_node

    def addInPosition(self, data: Kid, position: int):
        if self.__head is not None and position == 1:
            addToStart(Kid)
        else:
            if position <= self.__size + 1:
                pos = 1
                temp = self.__head
                while pos < position - 1:
                    temp = temp.get_next()
                    pos += 1

                new_node = NodeDE(data)
                new_node.set_next(temp.get_next())
                temp.set_next(new_node)
                new_node.set_previous(temp)

        self.__size += 1

    def deleteByPosition(self, position:int):
        if position == 1:
            self.__head = self.__head.get_next()
            if self.__head is not None:
                self.__head.set_previous(None)
        else:
            temp = self.__head
            pos = 1
            while pos < position - 1:
                temp = temp.get_next()
                pos += 1
            temp.set_next(temp.get_next().get_next())

            if temp.get_next() is not None:
                temp.get_next().set_previous(temp)

    def deleteById(self, id: int):
        if self.__head is None:
            return "No hay nodos"
        elif self.__head.get_data().id == id:
            self.__head = self.__head.get_next()

            if self.__head is not None:
                self.__head.set_previous(None)

            self.__size -= 1
            return "Borrado exitosamente"
        else:
            temp = self.__head
            while temp.get_next() is not None:
                if temp.get_next().get_data().id == id:
                    new_node = NodeDE(Kid)
                    temp.set_next(new_node.get_next())

                    if new_node.get_next() is not None:
                        new_node.get_next().set_previous(temp)
                    self.__size -= 1
                    return "Borrado exitosamente"
                temp = temp.get_next()

        return "No encontrado"

    def invert(self):
        if self.__head == None:
            return

        list_cp = ListDE()
        temp = self.__head
        while temp is not None:
            list_cp.addToStart(temp.get_data())
            temp = temp.get_next()
        self.__head = list_cp.get_head()

    def changeExtremes(self):
        if self.__head is None:
            return "No hay nada"
        else:
            temp = self.__head
            # Encuentra el último nodo
            while temp.get_next() is not None:
                temp = temp.get_next()

            new_kid = temp.get_data()
            temp.set_data(self.__head.get_data())
            self.__head.set_data(new_kid)
            return "Se cambiaron los extremos"

    def show(self):
        list_data = []
        if self.get_head() is not None:
            temp = self.get_head()
            while temp is not None:
                list_data.append(temp.get_data())
                temp = temp.get_next()
        return list_data
