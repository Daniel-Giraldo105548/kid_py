from pydantic import BaseModel

class Kid(BaseModel):
    id:str
    name:str
    age:int
    gender:str
class Node:
    def __init__(self, kid: Kid):
        self.__data = kid
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data:Kid):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

class ListSE:
    def __init__(self):
        self.__head = None
        self.size = 0

    def get_head(self):
        return self.__head

    def set_head(self, node):
        self.__head = node

    def get_size(self):
        return self.__size

    def set_size(self, size:int):
        self.__size = size

    # Metodo para agregar
    def add(self, data: Kid):
        if self.__head is None:
            self.__head = Node(data)
        else:
            temp = self.__head
            # Recorre la lista hasta el último nodo
            while temp.get_next() is not None:
                temp = temp.get_next()
            temp.set_next(Node(data))
        self.size += 1

    # Metodo para agregar a la cabeaza
    def addToStart(self, data:Kid):
        if self.__head == None:
            self.add(data)
        else:
            new_node = Node(data)
            new_node.set_next(self.__head)
            self.__head = new_node

        self.size += 1

    # Metodo para invertir
    def invert(self):
        if self.__head == None:
            return "No hay datos"
        else:
            list_cp = ListSE()
            temp = self.__head
            while temp is not None:
                list_cp.addToStart(temp.get_data())
                temp = temp.get_next()
            self.__head = list_cp.get_head()
            return "Se invertio"

    def addInPosition(self, data: Kid, position: int):
        new_node = Node(data)
        if position == 1:
            new_node.set_next(self.__head)
            self.__head = new_node
        else:
            pos = 1
            temp = self.__head

            while pos < position - 1 and temp is not None:
                temp = temp.get_next()
                pos += 1

            new_node.set_next(temp.get_next())
            temp.set_next(new_node)

        self.size += 1

    def deleteById(self, id: str):
        if self.__head is None:
            return "No hay nada"

        if self.__head.get_data().id == id:
            self.__head = self.__head.get_next()
            self.size -= 1
            return "Borrado exitosamente"
        else:
            temp = self.__head

            while temp.get_next() is not None:
                if temp.get_next().get_data().id == id:
                    temp.set_next(temp.get_next().get_next())
                    self.size -= 1
                    return "Borrado exitosamente"
                temp = temp.get_next()

            return "No se encontro"

    def deleteByPosition(self, position: int):
        if self.__head is None:
            return "No hay nada en la lista"

        if position < 1 or position > self.size:
            return "Posición inválida"

        # Si la posición es la primera (eliminar el nodo en la cabeza)
        if position == 1:
            self.__head = self.__head.get_next()
            return "Nodo en la posición 1 eliminado exitosamente"
            self.size -= 1
        else:
            temp = self.__head
            pos = 1
            while pos < position -1:
                temp = temp.get_next()
                pos += 1
        temp.set_next(temp.get_next)
        return "Se borro"
        self.size -= 1

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

    def mixByGender(self):
        if self.__head is None:
            return "No hay nada"
        if self.size >= 2:
            pos_b = 1
            pos_m = 1

            list_cp = ListSE()
            temp = self.__head
            while temp is not None:
                if temp.get_data().gender == "M" or temp.get_data().gender == "m":
                    list_cp.addInPosition(temp.get_data(), pos_b)
                    pos_b += 2
                elif temp.get_data().gender == "F" or temp.get_data().gender == "f":
                    list_cp.addInPosition(temp.get_data(), pos_m)
                    pos_m += 2

                temp = temp.get_next()
            self.__head = list_cp.get_head()
            return "Se intercalo bien"
