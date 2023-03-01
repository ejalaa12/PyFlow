from PyFlow.Core import NodeBase, PinBase
from PyFlow.Core.Common import PinOptions, StructureType
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
import numpy as np

class linspaceArray(NodeBase):
    def __init__(self, name):
        super(linspaceArray, self).__init__(name)
        self.start_value: PinBase = self.createInputPin('start', 'AnyPin',
                                                        structure=StructureType.Array,
                                                        constraint="1")
        self.end_value: PinBase = self.createInputPin('stop', 'AnyPin',
                                                      structure=StructureType.Array,
                                                      constraint="1")
        self.num_value: PinBase = self.createInputPin('num', 'AnyPin',
                                                      structure=StructureType.Array,
                                                      constraint="1")
        # self.start_value.enableOptions(PinOptions.AllowAny)

        # self.num_value.setDefaultValue(50)

        self.out_array = self.createOutputPin('array', 'NdArrayPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('AnyPin')
        helper.addInputDataType('AnyPin')
        helper.addInputDataType('AnyPin')
        helper.addInputStruct(StructureType.Array)
        helper.addInputStruct(StructureType.Array)
        helper.addInputStruct(StructureType.Array)
        helper.addOutputDataType('NdArrayPin')
        helper.addOutputStruct(StructureType.Array)
        return helper

    @staticmethod
    def category():
        return 'Numpy'

    @staticmethod
    def keywords():
        return ['linspace', 'numpy', 'np.linspace']

    @staticmethod
    def description():
        return "create np.linspace array"

    def compute(self, *args, **kwargs):
        out_array = np.linspace(self.start_value.getData(), self.end_value.getData(),
                             self.num_value.getData())
        print(out_array)

        self.out_array.setData(out_array)

