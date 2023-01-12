from PyFlow.UI.UIInterfaces import IPackage

from .Pins.NdArrayPin import NdArrayPin
from .Nodes.makeNumpyArray import makeNumpyArray


class PyFlowNumpy(IPackage):

    def __init__(self):
        super().__init__()

    @staticmethod
    def GetExporters():
        return {}

    @staticmethod
    def GetFunctionLibraries():
        return {}

    @staticmethod
    def GetNodeClasses():
        return {
            makeNumpyArray.__name__: makeNumpyArray
        }

    @staticmethod
    def GetPinClasses():
        return {
            NdArrayPin.__name__: NdArrayPin
        }

    @staticmethod
    def GetToolClasses():
        return {}
