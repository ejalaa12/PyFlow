from PyFlow.UI.Canvas.UIPinBase import UIPinBase
from PyFlow.Packages.PyFlowNumpy.Pins.NdArrayPin import NdArrayPin
from PyFlow.Packages.PyFlowNumpy.UI.UIDemoPin import UIDemoPin


def createUIPin(owningNode, raw_instance):
    if isinstance(raw_instance, DemoPin):
        return UIDemoPin(owningNode, raw_instance)
    else:
        return UIPinBase(owningNode, raw_instance)
