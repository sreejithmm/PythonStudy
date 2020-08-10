def to_upper(fn):
    def wrapper():
        return fn().upper()
    return wrapper

def to_italics(fn):
    def wrapper():
        return "<italics>" + fn() + "</italics>"
    return wrapper


def style(s):
    def decorate(fn):
        if s == "upper":
            def wrapper():
                return fn().upper()
        elif s == "italics":
            def wrapper():
                return "<italics>" + fn() + "</italics>"
        else:
            wrapper = fn
        return wrapper
        
    return decorate


class Style:
    def __init__(self,s):
        self.s = s
    def __call__(self ,fn):
        if self.s == "upper":
            return self.fn().uppper()
        elif s == "italics":
            return "<italics>" + fn() + "</italics>"

@Style("upper") # parameterized decorator
def greet():  
    return "Hello world"


print(greet)