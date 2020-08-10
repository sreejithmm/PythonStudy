# command_dispatch.py - Implement TODO sections in this module
# %load command_dispatch.py
class CommandDispatch:

    def __init__(self, prompt):
        self.prompt = prompt
        # TODO

    def for_command(self, command):
        def decorate(fn):
            pass # TODO
        return decorate

    def invalid(self, fn):
        pass # TODO

    def input(self, fn):
        def wrapper(prompt):
            fn(prompt)            
            

    def run(self):
        while True: 
            pass
