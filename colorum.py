import os

import colorama

colorama.init(convert=True)


class CharColor:
    def __init__(self, background=colorama.Back.RESET, foreground=colorama.Fore.RESET, value=" "):
        self.background = background
        self.foreground = foreground
        self.value = value

    def __repr__(self):
        return f"\"{self.background}\", \"{self.foreground}\", \"{self.value}"


class Screen:
    def __init__(self, background=colorama.Back.RESET, foreground=colorama.Fore.RESET, resolution=None):
        self.__resolution = resolution
        if resolution is None:
            self.__resolution = [640, 480]
        self.__background = background
        self.__foreground = foreground
        self.__current_screen = []
        self.__generate_screen(self.__background, self.__foreground)

    def __generate_screen(self, background=colorama.Back.RESET, foreground=colorama.Fore.RESET):
        row_list = []
        self.__current_screen = []
        for _ in range(0, self.__resolution[0]):
            for ii in range(0, self.__resolution[1]):
                row_list.append(CharColor(background, foreground))
            row_list.append(CharColor(colorama.Back.RESET, colorama.Fore.RESET, "\n"))
            self.__current_screen.append(row_list)
            row_list = []

    def set_resolution(self, resolution=None):
        if resolution is None:
            self.__resolution = [640, 480]
        self.__resolution = resolution

    def set_background(self, background=colorama.Back.RESET):
        self.__background = background
        self.__generate_screen(self.__background, self.__foreground)

    def set_foreground(self, foreground=colorama.Fore.RESET):
        self.__foreground = foreground
        self.__generate_screen(self.__background, self.__foreground)

    def insert_string(self, string="", background=colorama.Back.RESET, foreground=colorama.Fore.RESET, string_offset=0,
                      char_offset=0):

        for _ in range(len(string)):
            self.__current_screen[string_offset][char_offset + _] = CharColor(background, foreground, string[_])

    def print_screen(self):
        for row in self.__current_screen:
            for char in row:
                print(char.background + char.foreground + char.value + colorama.Back.RESET + colorama.Fore.RESET,
                      end="")

# Simple animation (slow)
#screen = Screen(background=colorama.Back.GREEN, resolution=[50, 200])
#offset = 0
#string_offset = 0
#for i in range(0, 200 * 50):
 #   if offset >= 200:
  #      offset = 0
   #     string_offset += 1
    #    screen.insert_string(" ", colorama.Back.CYAN, string_offset=string_offset, char_offset=offset)
     #   screen.print_screen()
      #  screen.set_background(colorama.Back.GREEN)
  #  else:
   #     offset += 1
    #    screen.insert_string(" ", colorama.Back.CYAN, string_offset=string_offset, char_offset=offset)
     #   screen.print_screen()
      #  screen.set_background(colorama.Back.GREEN)
   # os.system("cls")
