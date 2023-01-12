from PyFlow.Core import PinBase
import numpy as np


class NdArrayPin(PinBase):

    def __init__(self, name, parent, direction, **kwargs):
        super(NdArrayPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(np.empty([1], dtype=np.float))

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def color():
        return 1, 49, 65, 255

    @staticmethod
    def pinDataTypeHint():
        return 'NdArrayPin', 0

    @staticmethod
    def internalDataStructure():
        return np.array

    @staticmethod
    def processData(data):
        return NdArrayPin.internalDataStructure()(data)


