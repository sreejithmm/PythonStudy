from command_dispatcher import CommandDispatch

shell = CommandDispatch("PyShell> ")

@shell.for_command("list")
def list_directory(*args):
    from os import listdir
    if len(args) < 2:
        args += ".",
    for path in args[1:]:
        print("{}:".format(path))
        print("\n".join(listdir(path)))

@shell.for_command("whoami")
def show_user(*args):
    from getpass import getuser
    print(getuser())

@shell.for_command("date")
def print_date(*args):
    from time import ctime
    print(ctime())

@shell.for_command("exit")
def exit_shell(*args):
    exit(0)

@shell.invalid
def invalid_command(*args):
    print("Invalid command - ", args[0])


@shell.input
def get_input(prompt):
    return input(prompt).split()


if __name__ == '__main__':
    shell.run()

