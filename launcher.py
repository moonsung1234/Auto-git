
import os
import time
import threading

class Setter :
    def __init__(self, command, before_setter) :
        self.command = command
        self.setter = before_setter

class Launcher :
    def __init__(self) :
        self.thread = None
        self.cycle = None

    def __run(self, setter) :
        while True :
            if setter.name == "master" :
                temp = setter.head_setter.setter
            
            else :
                temp = setter.head_setter

            while temp != None :
                state = os.system(temp.command)

                if state != 0 :
                    raise Exception("Error state : " + str(state))
                    return

                temp = temp.setter

            if self.cycle == None :
                break

            time.sleep(self.cycle)

    def setCycle(self, cycle) :
        self.cycle = cycle

    def run(self, setter) :
        self.thread = threading.Thread(target=self.__run, args=(setter,))
        self.thread.start()

        return self.thread