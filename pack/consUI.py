def Input(headMesage):
    """Standart console command input"""
    return input(headMesage + '>')

def Output(message):
    print('\n{}\n'.format(message))

def ConfirmDialog(message):
    """Show confirm dialog"""
    result = None
    while result is None:
        print(message + "(y/n):", end=' ')
        answer = input().lower()
        if answer in ['y', "yes"]:
            result = True
        elif answer in ['n', "no"]:
            result = False
        else:
            print("Uncorect input")
    return result

class ComandLine:
    """Console menu"""
    def __init__(self, head='', closeAlias=None):
        self.headMes = head
        self.commands = []
        self.exitCommands = []
        self.showing = True
        if not closeAlias is None:
            self.AddExit(closeAlias)

    def Show(self):
        while self.showing:
            command = Input(self.headMes)
            if command in self.exitCommands:
                self.Exit()
                break
            for c in self.commands:
                if command in c[0]:
                    c[1]()
                    break
            else:
                self.UnknowCommand()

    def AddCommand(self, alias, delegate):
        """Add command"""
        self.commands.append((alias, delegate))

    def AddExit(self, alias):
        self.exitCommands = alias

    def UnknowCommand(self):
        print('Unsupported command!')

    def Exit(self):
        self.showing = False
    

