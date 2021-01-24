
import os
import time
import datetime
import threading

class Setter :
    def __init__(self, command, setter) :
        self.command = command
        self.setter = setter

class Launcher :
    def __init__(self) :
        self.thread = None
        self.date = None
        self.cycle = None

    def __loopSetter(self, setter) :
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

    def __run(self, setter) :
        while True :
            if self.date != None :
                date_now = datetime.datetime.now()

                if self.date[0] == date_now.year \
                and self.date[1] == date_now.month \
                and self.date[2] == date_now.day \
                and self.date[3] == date_now.hour :
                    self.__loopSetter(setter)
            
            else :
                self.__loopSetter(setter)

            if self.cycle != None :
                time.sleep(self.cycle)

            else :
                break

    def setDate(self, date) :
        self.date = list(map(int, date.split("/")))

    def setCycle(self, cycle) :
        self.cycle = cycle

    def run(self, setter) :
        self.thread = threading.Thread(target=self.__run, args=(setter,))
        self.thread.start()

        return self.thread