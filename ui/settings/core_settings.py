from tkinter import LabelFrame, Frame, Label, Entry
from tkinter import LEFT, Button, CENTER, BOTTOM, X


class CoreSettings():
    def __init__(self, parent):
        self.parent = parent

        self.color_group = LabelFrame(parent, text="Core Colors", padx=5, pady=5)
        self.color_group.pack(fill=X)

        self.colors = []

        self.add_color_field()
        self.add_color_field()

        self.add_plus_button()


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


        self.colors.append({
            'hex': color_entry,
            'prio': prio_entry
        })

    def add_plus_button(self):
        """Add Plus Button to generate extra color fields

        Elements:
            - Button
        """
        plus_button = Button(
            master=self.color_group,
            text='+',
            command=self.add_color_field,
            justify=CENTER
        )

        plus_button.pack(side=BOTTOM)
