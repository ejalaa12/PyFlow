from collections import Counter
from collections import defaultdict

from Qt import QtCore

from PyFlow.Core.Common import *


class InputAction(object):
    def __init__(self, name="defaultName", group="default", mouse=QtCore.Qt.MouseButton.NoButton, keys=[], modifiers=QtCore.Qt.NoModifier):
        self._name = name
        self._group = group
        self.__data = {"mouse": mouse, "keys": keys, "modifiers": modifiers}

    def __eq__(self, other):
        # TODO: compare name and group?
        sm = self.__data["mouse"]
        sk = self.__data["keys"]
        smod = self.__data["modifiers"]
        om = other.getData()["mouse"]
        ok = other.getData()["keys"]
        omod = other.getData()["modifiers"]
        smod == omod
        return all([sm == om,
                    Counter(sk) == Counter(ok),
                    smod == omod])

    def __ne__(self, other):
        sm = self.__data["mouse"]
        sk = self.__data["keys"]
        smod = self.__data["modifiers"]
        om = other.getData()["mouse"]
        ok = other.getData()["keys"]
        omod = other.getData()["modifiers"]
        return not all([sm == om,
                        Counter(sk) == Counter(ok),
                        smod == omod])

    def getName(self):
        return self._name

    def getData(self):
        return self.__data

    def setMouseButton(self, btn):
        assert(isinstance(btn, QtCore.Qt.MouseButton))
        self.__data["mouse"] = btn

    def setKeys(self, keys=[]):
        for i in keys:
            assert(isinstance(i, QtCore.Qt.Key))
        self.__data["keys"] = keys

    def getKeys(self):
        return self.__data["keys"]

    def containsKeys(self, keysList=[]):
        return Counter(self.__data["keys"]) == Counter(keysList)

    def setModifiers(self, modifiers=[]):
        self.__data["modifiers"] = modifiers

    def getModifiers(self):
        return self.__data["modifiers"]

    @staticmethod
    def _modifiersToList(mods):
        result = []
        if mods & QtCore.Qt.ShiftModifier:
            result.append(QtCore.Qt.ShiftModifier)
        if mods & QtCore.Qt.ControlModifier:
            result.append(QtCore.Qt.ControlModifier)
        if mods & QtCore.Qt.AltModifier:
            result.append(QtCore.Qt.AltModifier)
        if mods & QtCore.Qt.MetaModifier:
            result.append(QtCore.Qt.MetaModifier)
        if mods & QtCore.Qt.KeypadModifier:
            result.append(QtCore.Qt.KeypadModifier)
        if mods & QtCore.Qt.GroupSwitchModifier:
            result.append(QtCore.Qt.GroupSwitchModifier)
        return result

    def _listOfModifiersToEnum(self, modifiersList):
        result = QtCore.Qt.NoModifier
        for mod in modifiersList:
            result = result | mod
        return result

    def toJson(self):
        saveData = {}
        saveData["name"] = self._name
        saveData["group"] = self._group
        saveData["mouse"] = int(self.__data["mouse"])
        saveData["keys"] = [int(i) for i in self.__data["keys"]]
        modifiersList = self._modifiersToList(self.__data["modifiers"])
        saveData["modifiers"] = [int(i) for i in modifiersList]
        return saveData

    def fromJson(self, jsonData):
        try:
            self._name = jsonData["name"]
            self._group = jsonData["group"]
            self.__data["mouse"] = QtCore.Qt.MouseButton(jsonData["mouse"])
            self.__data["keys"] = [QtCore.Qt.Key(i) for i in jsonData["keys"]]
            self.__data["modifiers"] = self._listOfModifiersToEnum([QtCore.Qt.KeyboardModifier(i) for i in jsonData["modifiers"]])
            return self
        except:
            return None


@SingletonDecorator
class InputManager(object):
    """Holds all registered input actions."""

    def __init__(self, *args, **kwargs):
        self.__actions = defaultdict(list)

    def __getitem__(self, key):
        # try find input action by name
        if key in self.__actions:
            return self.__actions[key]
        return []

    def __contains__(self, item):
        return item.getName() in self.__actions

    def registerAction(self, action):
        self.__actions[action.getName()].append(action)

    def loadFromData(self, data):
        for actionName, actionVariants in data.items():
            for variant in actionVariants:
                actionInstance = InputAction().fromJson(variant)
                self.registerAction(actionInstance)

    def serialize(self):
        result = defaultdict(list)
        for actionName in self.__actions:
            for actionVariant in self.__actions[actionName]:
                result[actionName].append(actionVariant.toJson())
        return result