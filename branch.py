
import os
import copy
import gitstring as gs
from launcher import Setter

class Branch :
    def __fcheckoutBranch(self, name) :
        setter = Setter(gs.checkout(name), None)

        self.head_setter = setter
        self.setter = setter

    def __init__(self, name) :
        self.name = name
        self.__fcheckoutBranch(self.name)        

    def addFile(self, _file) :
        setter = Setter(gs.add(_file), None)

        self.setter.setter = setter
        self.setter = setter

        return setter

    def commit(self, name) :
        setter = Setter(gs.commit(name), None)

        self.setter.setter = setter
        self.setter = setter

        return setter

    def push(self, url) :
        setter = Setter(gs.push(url, self.name), None)

        self.setter.setter = setter
        self.setter = setter

        return setter
        
    