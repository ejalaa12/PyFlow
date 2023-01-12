from PyFlow.Core import NodeBase, PinBase
from PyFlow.Core.Common import PinOptions, StructureType
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
import numpy as np
import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


class makeNumpyArray(NodeBase):
    def __init__(self, name):
        super().__init__(name)
        self.arrayData: PinBase = self.createInputPin('data', 'AnyPin',
                                                  structure=StructureType.Array, constraint="1")
        self.arrayData.enableOptions(PinOptions.AllowMultipleConnections)
        self.arrayData.disableOptions(PinOptions.SupportsOnlyArrays)

        self.out_array = self.createOutputPin('array', 'NdArrayPin', structure=StructureType.Array, constraint="1")
        self.result = self.createOutputPin('success', 'BoolPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('AnyPin')
        helper.addInputDataType('BoolPin')
        helper.addOutputDataType('AnyPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Array)
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Array)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'GenericTypes'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Creates an array from connected pins'

    def compute(self, *args, **kwargs):
        outArray = []
        ySortedPins = sorted(self.arrayData.affected_by, key=lambda pin: pin.owningNode().y)

        for i in ySortedPins:
            if isinstance(i.getData(), list):
                for e in i.getData():
                    outArray.append(e)
            # todo
            # elif isinstance(i.getData(), np.ndarray):
            #     for e in i.getData():
            #         outArray.append(e)
            else:
                outArray.append(i.getData())

        self.out_array.setData(outArray)
        self.arrayData.setData(outArray)
        self.result.setData(True)

    # def deserialize(self, jsonData):
    #     json.loads(jsonData)
    #
    # def serialize(self):
    #     return super().serialize()
