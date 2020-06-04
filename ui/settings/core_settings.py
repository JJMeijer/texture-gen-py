from tkinter import LabelFrame, Frame, Label, Entry
from tkinter import LEFT, Button, CENTER, BOTTOM, X


class CoreSettings():
    def __init__(self, parent):
        self.parent = parent

        self.color_group = LabelFrame(parent, text="Core Colors", padx=5, pady=5)
        self.color_group.pack(fill=X)

        self.colors = []

        self.add_color_field("#362417", 80) # Default color field 1
        self.add_color_field("#2b1d12", 20) # Default color field 2

        self.add_plus_button()


    def add_color_field(self, default_hex=None, default_prio=None):
        """Add Input field for colors

        :param default_hex: default hex value, defaults to None
        :type default_hex: str, optional
        :param default_prio: default prio value, defaults to None
        :type default_prio: int, optional

        Elements:
            - Frame
                - Hex Label
                - Hex Entry

                - Prio Label
                - Prio Entry
        """
        master = self.color_group

        color_field = Frame(master)
        color_field.pack()

        Label(master=color_field, text='Hex').pack(side=LEFT)
        color_entry = Entry(master=color_field, width=20)
        color_entry.pack(side=LEFT)
        if default_hex is not None:
            color_entry.insert(0, default_hex)

        Label(master=color_field, text='Prio').pack(side=LEFT)
        prio_entry = Entry(master=color_field, width=10)
        prio_entry.pack(side=LEFT)
        if default_prio is not None:
            prio_entry.insert(0, default_prio)

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
