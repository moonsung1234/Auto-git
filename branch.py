
import os
import gitstring as gs

class Branch :
    def __checkoutBranch(self, name) :
        if name != "master" :
            checkout_state = os.system(gs.checkout(name))

            if checkout_state != 0 :
                branch_state = os.system(gs.branch(name))
                recheckout_state = os.system(gs.checkout(name))

                if recheckout_state != 0 :
                    raise Exception("Error state : " + str(recheckout_state))
                    return

    def __init__(self, name) :
        self.name = name
        self.__checkoutBranch(name)

    def addFile(self, _file) :
        add_state = os.system(gs.add(_file))

        if add_state != 0 :
            raise Exception("Error state : " + str(add_state))
            return

    def commit(self, name) :
        commit_state = os.system(gs.commit(name))

        if commit_state != 0 :
            raise Exception("Error state : " + str(commit_state))
            return

    def push(self, url) :
        push_state = os.system(gs.push(url, self.name))

        if push_state != 0 :
            raise Exception("Error state : " + str(push_state))
            return
    