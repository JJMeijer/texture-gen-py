from tkinter import LabelFrame, Frame, Label, Entry
from tkinter import LEFT, X


class SizeSettings():
    def __init__(self, parent):
        self.parent = parent

        self.size_group = LabelFrame(parent, text="Size", padx=5, pady=5)
        self.size_group.pack()

        self.width = None
        self.height = None

        self.generate_size_field()


    def generate_size_field(self):
        """Generate Size Input field

        Elements:
            - Frame
                - Width Label
                - Width Entry

                - Height Label
                - Height Entry
        """
        master = self.size_group

        size_field = Frame(master)
        size_field.pack(fill=X)

        Label(master=size_field, text='Width').pack(side=LEFT)
        width_entry = Entry(master=size_field, width=15)
        width_entry.pack(side=LEFT)
        width_entry.insert(0, '20')

        Label(master=size_field, text='Height').pack(side=LEFT)
        height_entry = Entry(master=size_field, width=15)
        height_entry.pack(side=LEFT)
        height_entry.insert(0, '20')

        self.width = width_entry
        self.height = height_entry
