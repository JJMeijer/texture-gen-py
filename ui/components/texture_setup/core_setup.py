import re

from tkinter import LabelFrame, Frame, Label, Entry, Button
from tkinter import LEFT, RIGHT, CENTER, BOTTOM, TOP, X


class CoreSetup():
    def __init__(self, parent):
        self.parent = parent

        self.core_group = LabelFrame(parent, text="Core Colors", padx=5, pady=5)
        self.core_group.pack(fill=X)

        self.color_group = Frame(master=self.core_group)
        self.color_group.pack(side=TOP)

        self.palette = []

        self.add_color_field()
        self.add_color_field()

        self.add_buttons()


    def flush_colors(self):
        self.palette = []

        color_entries = self.color_group.children
        delete_list = []
        for child in color_entries:
            if re.search('frame', child):
                color_entries[child].pack_forget()
                delete_list.append(color_entries[child])

        while len(delete_list) > 0:
            child = delete_list.pop()
            child.destroy()


    def add_color_field(self, color=None):
        """Add Input field for colors

        :param color: Color values to put in the entries, defaults to None
        :type color: dict, optional
        """
        master = self.color_group

        color_field = Frame(master)
        color_field.pack()

        Label(master=color_field, text='Hex').pack(side=LEFT)
        color_entry = Entry(master=color_field, width=20)
        color_entry.pack(side=LEFT)

        Label(master=color_field, text='Prio').pack(side=LEFT)
        prio_entry = Entry(master=color_field, width=10)
        prio_entry.pack(side=LEFT)

        if color is not None:
            color_entry.insert(0, color['hex'])
            prio_entry.insert(0, color['prio'])
        else:
            prio_entry.insert(0, 1)


        self.palette.append({
            'hex': color_entry,
            'prio': prio_entry
        })


    def remove_color_field(self):
        color_entries = self.color_group.children

        if len(self.palette) > 0:
            self.palette.pop()

        if len(color_entries) > 0:
            last_color = color_entries.popitem()[1]
            last_color.pack_forget()
            last_color.destroy()


    def add_buttons(self):
        button_frame = Frame(self.core_group)
        button_frame.pack(side=BOTTOM)

        plus_button = Button(
            master=button_frame,
            text='+',
            command=self.add_color_field,
            justify=CENTER
        )

        plus_button.config(
            width=2,
            height=1
        )

        plus_button.pack(side=LEFT)

        minus_button = Button(
            master=button_frame,
            text='-',
            command=self.remove_color_field,
            justify=CENTER
        )

        minus_button.config(
            width=2,
            height=1
        )

        minus_button.pack(side=RIGHT)
