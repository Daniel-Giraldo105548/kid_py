from model import model

class ListSEService:
    def __init__(self):
        self.__kids = model.ListSE()

    def get_kids(self):
        return self.__kids
