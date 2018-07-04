"""Console UI elements"""
def read(message):
    """Cconsole command input"""
    return input("{}>".format(message))

def write(message):
    """Console write"""
    print("\n{}\n".format(message))

def confirm(message):
    """Show confirm dialog"""
    positive = ['y', "yes"]
    negative = ['n', "no"]
    result = [None]
    def set_res(arg):
        result[0] = arg
    promt = CommandPromt(message, single=True)
    promt.add_command(positive, lambda: set_res(True))
    promt.add_command(negative, lambda: set_res(False))
    promt.show()
    return result[0]


class MenuList:
    """Menu with some options"""
    def __init__(self, name=''):
        self.name = name
        self._command_line = CommandPromt(self.name, single=True)
        self._option_names = ''
        self._option_num = 0

    def show(self):
        """Show menu"""
        write(self._option_names)
        self._command_line.show()

    def add_option(self, name, delegate):
        """Add option to menu"""
        self._option_num += 1
        num = self._option_num
        self._command_line.add_command((str(num),), delegate)
        if self._option_names != '':
            self._option_names += '\n'
        self._option_names += "{0}. {1}".format(num, name)


class CommandPromt:
    """Command line input"""
    def __init__(self, head='', close_alias=None, single=False):
        self._head_message = head
        self._commands = []
        self._exit_commands = []
        self._showing = not single
        if close_alias is not None:
            self._add_exit(close_alias)

    def show(self):
        """Begin input in command promt"""
        while True:
            right_command = False
            while not right_command:
                command = read(self._head_message)
                if command in self._exit_commands:
                    right_command = True
                    self._exit()
                    break
                for c in self._commands:
                    if command in c[0]:
                        right_command = True
                        c[1]()
                        break
                else:
                    write('Unsupported command!')
            if not self._showing:
                break

    def add_command(self, alias, delegate):
        """Add command"""
        self._commands.append((alias, delegate))

    def _add_exit(self, alias):
        """Add exit alias"""
        self._exit_commands += alias

    def _exit(self):
        """Close command promt"""
        self._showing = False
