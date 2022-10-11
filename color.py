

class Color:  # object whit colors as attributes
    def __init__(self):
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.blue = '\033[34m'
        self.ciano = '\033[36m'
        self.magenta = '\033[35m'
        self.yellow = '\033[33m'
        self.black = '\033[30m'
        self.white = '\033[37m'
        self.reset = '\033[0;0m'
        self.bold = '\033[1m'
        self.reversed = '\033[2m'
        self.black_Background = '\033[40m'
        self.red_Background = '\033[41m'
        self.green_Background = '\033[42m'
        self.yellow_Background = '\033[43m'
        self.blue_Background = '\033[44m'
        self.magenta_Background = '\033[45m'
        self.ciano_Background = '\033[45m'
        self.white_Background = '\033[45m'


colors = Color()
