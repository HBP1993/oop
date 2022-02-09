class CellPhone:
    def __inti__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__module = model
        self.__price = retail_price

    def set_manufact(self, manufact):
        self._manufact = manufact

        # return self.set_manufact

    def set_model(self, model):
        self._model = model

    def set_retail_price(self, retail_price):
        self._retail_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self._model

    def get_retail_price(self):
        return self._retail_price
