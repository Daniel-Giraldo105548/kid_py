from model import model

class ListDEService:

    def __init__(self):
        self.__kids = model.ListDE()


    def get_kids(self):
        return self.__kids