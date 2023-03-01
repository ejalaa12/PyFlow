from collections import OrderedDict

PACKAGE_NAME = 'PyFlowNumpy'
from PyFlow.UI.UIInterfaces import IPackage

from .Pins.NdArrayPin import NdArrayPin
from .Nodes.makeNumpyArray import makeNumpyArray
from .Nodes.linspaceArray import linspaceArray
from .FunctionLibraries.Numpy import Numpy
from .FunctionLibraries.Datetime import Datetime


class PyFlowNumpy(IPackage):

    def __init__(self):
        super().__init__()

    @staticmethod
    def GetExporters():
        return OrderedDict()

    @staticmethod
    def GetFunctionLibraries():
        return {
            Numpy.__name__: Numpy(PACKAGE_NAME),
            Datetime.__name__: Datetime(PACKAGE_NAME)
        }

    @staticmethod
    def GetNodeClasses():
        return {
            makeNumpyArray.__name__: makeNumpyArray,
            linspaceArray.__name__: linspaceArray
        }

    @staticmethod
    def GetPinClasses():
        return {
            NdArrayPin.__name__: NdArrayPin
        }

    @staticmethod
    def GetToolClasses():
        return OrderedDict()

    # @staticmethod
    # def UIPinsFactory():
    #     return createUIPin
    #
    # @staticmethod
    # def UINodesFactory():
    #     return createUINode
    #
    # @staticmethod
    # def PinsInputWidgetFactory():
    #     return getInputWidget
    #
    # @staticmethod
    # def PrefsWidgets():
    #     return None
