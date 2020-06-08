import re

from tkinter import Frame, LabelFrame, Label, Button, Entry, OptionMenu, StringVar
from tkinter import LEFT, RIGHT, CENTER, BOTTOM, X, TOP


class EdgeSetup():
    def __init__(self, master):
        self.master = master

        self.edge_group = LabelFrame(master, text="Edges", padx=5, pady=10)
        self.edge_group.pack(fill=X)

        self.edges = []

        self.add_edge_frame()

        self.add_edge_button(master=self.edge_group)


    def add_edge_frame(self, side='top', width=2, palette=None):
        """Add Edge Frame and add side_field, width_field & color_field

        Elements:
            - LabelFrame
        """
        edge_n = len(self.edges)
        if edge_n < 4:
            master = self.edge_group

            edge_group = LabelFrame(master, text=f'Edge {edge_n + 1}', padx=5, pady=5)
            edge_group.pack()

            edge_settings = {
                'side': None,
                'width': None,
                'palette': []
            }

            self.edges.append(edge_settings)

            edge_dims = Frame(master=edge_group)
            edge_dims.pack(side=TOP)

            edge_color_setup = LabelFrame(master=edge_group, text="Edge Colors", padx=5, pady=5)
            edge_color_setup.pack(side=BOTTOM)

            edge_color_group = Frame(master=edge_color_setup)
            edge_color_group.pack(side=TOP)

            self.add_side_field(
                master=edge_dims,
                edge_settings=edge_settings,
                side=side
            )

            self.add_width_field(
                master=edge_dims,
                edge_settings=edge_settings,
                width=width
            )

            if palette is not None:
                for color in palette:
                    self.add_color_field(
                        color_group=edge_color_group,
                        edge_settings=edge_settings,
                        color=color
                    )
            else:
                self.add_color_field(
                    color_group=edge_color_group,
                    edge_settings=edge_settings,
                    color=None
                )

            self.add_color_buttons(
                master=edge_color_setup,
                color_group=edge_color_group,
                edge_settings=edge_settings
            )


    def add_side_field(self, master, edge_settings, side):
        """Add Side field to input which side this edge describes

        :param master: Master Tkinter object of this object
        :type master: class
        :param edge_settings: Dictionary that is used to store the OptionMenu object
        :type edge_settings: dict
        :param side: Value to put into the side Entry field
        :type side: string
        """
        side_var = StringVar(master)
        side_var.set(side)

        Label(master, text='Side:', padx=5).pack(side=LEFT)
        side_entry = OptionMenu(master, side_var, "top", "right", "bottom", "left")
        side_entry.pack(side=LEFT)

        edge_settings['side'] = side_var


    def add_width_field(self, master, edge_settings, width):
        """Add Field to set Width of Edge

        :param master: Tkinter object that is the master of this object
        :type master: class
        :param edge_settings: Dictionary that is used to store the Entry object
        :type edge_settings: dict
        :param width: width value for the Entry field
        :type width: int

        """
        Label(master, text='Width:', padx=5).pack(side=LEFT)
        width_entry = Entry(master, width=5)
        width_entry.pack(side=LEFT)
        width_entry.insert(0, width)

        edge_settings['width'] = width_entry


    def add_color_field(self, color_group, edge_settings, color):
        """Add Color Entry fram with an Hex & prio Entry

        :param color_group: Master tkinter element
        :type color_group: class
        :param edge_settings: Dictionary containing all edge settings Entry elements
        :type edge_settings: dict
        :param color: Dictionary with values to put into the entry fields on creation
        :type color: dict
        """
        color_field = Frame(color_group)
        color_field.pack()

        Label(color_field, text='Hex:').pack(side=LEFT)
        color_entry = Entry(color_field, width=20)
        color_entry.pack(side=LEFT)

        Label(color_field, text='Prio:').pack(side=LEFT)
        prio_entry = Entry(color_field, width=10)
        prio_entry.pack(side=LEFT)

        if color is not None:
            color_entry.insert(0, color['hex'])
            prio_entry.insert(0, color['prio'])
        else:
            prio_entry.insert(0, 1)

        edge_settings['palette'].append({
            'hex': color_entry,
            'prio': prio_entry
        })


    def remove_color_field(self, color_group, edge_settings):
        if len(edge_settings['palette']) > 0:
            edge_settings['palette'].pop()

        color_entries = color_group.children
        if len(color_entries) > 0:
            last_color = color_entries.popitem()[1]
            last_color.pack_forget()
            last_color.destroy()


    def add_color_buttons(self, master, color_group, edge_settings):
        button_frame = Frame(master)
        button_frame.pack(side=BOTTOM)

        plus_button = Button(
            button_frame,
            text='+',
            justify=CENTER,
            command=lambda: self.add_color_field(
                color_group=color_group,
                edge_settings=edge_settings,
                color=None
            )
        )

        plus_button.config(width=2, height=1)
        plus_button.pack(side=LEFT)

        minus_button = Button(
            button_frame,
            text='-',
            justify=CENTER,
            command=lambda: self.remove_color_field(
                color_group=color_group,
                edge_settings=edge_settings
            )
        )

        minus_button.config(width=2, height=1)
        minus_button.pack(side=RIGHT)


    def add_edge_button(self, master):
        """Add Plus Button to generate extra edge frames

        Elements:
            - Button
        """
        plus_button = Button(
            master=master,
            text='+',
            command=self.add_edge_frame,
            justify=CENTER
        )
        plus_button.pack(side=BOTTOM)


    def flush_edges(self):
        self.edges = []

        edge_entries = self.edge_group.children
        delete_list = []
        for child in edge_entries:
            if re.search('labelframe', child):
                edge_entries[child].pack_forget()
                delete_list.append(edge_entries[child])

        while len(delete_list) > 0:
            child = delete_list.pop()
            child.destroy()
