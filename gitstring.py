
def init() :
    return "git init" 

def url(name, url) :
    return "git remote add " + name + " " + url

def branch(name) :
    return "git branch " + name

def checkout(name) :
    return "git checkout " + name

def add(_file) : 
    return "git add " + _file

def commit(name) :
    return "git commit -m " + name

def push(url, branch) :
    return "git push " + url + " " + branch
