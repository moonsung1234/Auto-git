
import os

class Setter :
    def __init__(self, command, before_setter) :
        self.command = command
        self.setter = before_setter

class Launcher :
    def run(self, setter) :
        temp = setter.head_setter

        while temp != None :
            state = os.system(temp.command)

            if state != 0 :
                raise Exception("Error state : " + str(state))
                return

            temp = temp.setter