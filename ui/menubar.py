from tkinter import Menu

class MenuBar():
    def __init__(self, window, reset_command):
        self.window = window
        self.reset_command = reset_command

        self.menubar = self.add_menu_bar()
        self.window.config(menu=self.menubar)


    def add_menu_bar(self):
        """Add tkinter menubar"""
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        file_menu = self.add_file_menu(menubar)
        menubar.add_cascade(label='File', menu=file_menu)

        return menubar


    def add_file_menu(self, parent):
        """Return a file Menu with items

        :param parent: Tkinter parent of the file_menu
        :type parent: class
        :return: class
        :rtype: tkinter menu class containing the file menu
        """
        file_menu = Menu(parent, tearoff=0)
        file_menu.add_command(
            label='Reset',
            command=self.reset_command
        )

        file_menu.add_command(
            label='Exit',
            command=self.exit_command
        )

        return file_menu


    def exit_command(self):
        """Quit the window"""
        self.window.quit()
