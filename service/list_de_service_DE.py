from model import model_DE

class ListDEService:
    def __init__(self):
        self.__kids = model_DE.ListDE()

    def get_kids(self):
        return self.__kids

    def show_kids(self):
        return self.__kids.show()

