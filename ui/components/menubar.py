from tkinter import Menu
from .texture_setup import DefaultSetup


class MenuBar:
    def __init__(self, root):
        self.root = root
        self.window = root.window

        self.menubar = self.add_menu_bar()
        self.window.config(menu=self.menubar)

    def add_menu_bar(self):
        """Add tkinter menubar"""
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        file_menu = self.add_file_menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)

        return menubar

    def add_file_menu(self, parent):
        """Return a file Menu with items

        :param parent: Tkinter parent of the file_menu
        :type parent: class
        :return: class
        :rtype: tkinter menu class containing the file menu
        """
        file_menu = Menu(parent, tearoff=0)
        file_menu.add_command(label="Reset", command=self.reset_command)

        file_menu.add_separator()

        file_menu.add_command(label="Save Setup", command=self.save_setup_command)

        file_menu.add_command(label="Load Setup", command=self.load_setup_command)

        file_menu.add_separator()

        file_menu.add_command(label="Export Image", command=self.export_command)

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=self.exit_command)

        return file_menu

    def reset_command(self):
        self.root.setup.process_import(DefaultSetup)
        self.root.texture_canvas.gen_image()

    def save_setup_command(self):
        self.root.setup.process_save_setup()

    def load_setup_command(self):
        self.root.setup.process_load_setup()

    def export_command(self):
        self.root.texture_canvas.export_image()

    def exit_command(self):
        """Quit the window"""
        self.window.quit()
