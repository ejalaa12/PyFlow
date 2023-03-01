from typing import Any, Callable

from PyFlow.Core import PinBase
import numpy as np
import json
from json import JSONEncoder, JSONDecoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

class NumpyArrayDecoder(JSONDecoder):

    def decode(self, s: str, _w: Callable[..., Any] = ...) -> Any:
        return np.array(super().decode(s, _w))


class NdArrayPin(PinBase):

    def __init__(self, name, parent, direction, **kwargs):
        super(NdArrayPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(np.empty([1], dtype=np.float64))

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def color():
        return 1, 49, 65, 255

    @staticmethod
    def pinDataTypeHint():
        return 'NdArrayPin', np.zeros([0])

    @staticmethod
    def internalDataStructure():
        return np.array

    @staticmethod
    def processData(data):
        return NdArrayPin.internalDataStructure()(data)

    @staticmethod
    def supportedDataTypes():
        return ('IntPin', 'FloatPin', 'AnyPin', 'NdArrayPin')

    @staticmethod
    def jsonEncoderClass():
        return NumpyArrayEncoder

    @staticmethod
    def jsonDecoderClass():
        return NumpyArrayDecoder







