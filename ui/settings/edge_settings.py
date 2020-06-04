from tkinter import Frame, LabelFrame, Label, Button, Entry, OptionMenu, StringVar
from tkinter import LEFT, CENTER, BOTTOM, X, TOP


class EdgeSettings():
    def __init__(self, master):
        self.master = master

        self.edge_group = LabelFrame(master, text="Edges", padx=5, pady=5)
        self.edge_group.pack(fill=X)

        self.edges = []

        self.add_edge_frame()

        self.add_edge_button(master=self.edge_group)


    def add_edge_frame(self):
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
                'colors': []
            }

            self.edges.append(edge_settings)

            edge_dims = Frame(master=edge_group)
            edge_dims.pack(side=TOP)

            edge_colors = Frame(master=edge_group)
            edge_colors.pack(side=BOTTOM)

            self.add_side_field(master=edge_dims, edge_settings=edge_settings)
            self.add_width_field(master=edge_dims, edge_settings=edge_settings)

            self.add_color_field(
                master=edge_colors,
                edge_settings=edge_settings,
                default_hex="#0b6623",
                default_prio=90
            )

            self.add_color_field(
                master=edge_colors,
                edge_settings=edge_settings,
                default_hex="#109433",
                default_prio=10
            )

            self.add_color_button(master=edge_colors, edge_settings=edge_settings)


    def add_side_field(self, master, edge_settings):
        """Add Side field to input which side this edge describes

        :param master: Master Tkinter object of this object
        :type master: class
        :param edge_settings: Dictionary that is used to store the OptionMenu object
        :type edge_settings: dict
        """
        side_var = StringVar(master)
        side_var.set('top')

        Label(master, text='Side:', padx=5).pack(side=LEFT)
        side_entry = OptionMenu(master, side_var, "top", "right", "bottom", "left")
        side_entry.pack(side=LEFT)

        edge_settings['side'] = side_var


    def add_width_field(self, master, edge_settings):
        """Add Field to set Width of Edge

        :param master: Tkinter object that is the master of this object
        :type master: class
        :param edge_settings: Dictionary that is used to store the Entry object
        :type edge_settings: dict
        """
        Label(master, text='Width:', padx=5).pack(side=LEFT)
        width_entry = Entry(master, width=5)
        width_entry.pack(side=LEFT)
        width_entry.insert(0, '2')

        edge_settings['width'] = width_entry


    def add_color_field(self, master, edge_settings, default_hex=None, default_prio=None):
        """Generate Input field for colors

        :param master: Tkinter object that is the master of this object
        :type master: class
        :param edge_settings: Dictionary that is used to store the Entry object
        :type edge_settings: dict
        :param default_hex: Default color hex value, defaults to None
        :type default_hex: str, optional
        :param default_prio: Default color prio value, defaults to None
        :type default_prio: int, optional

        Elements:
            - Frame
                - Hex Label
                - Hex Entry

                - Prio Label
                - Prio Entry
        """
        color_field = Frame(master)
        color_field.pack()

        Label(color_field, text='Hex:').pack(side=LEFT)
        color_entry = Entry(color_field, width=20)
        color_entry.pack(side=LEFT)
        if default_hex is not None:
            color_entry.insert(0, default_hex)

        Label(color_field, text='Prio:').pack(side=LEFT)
        prio_entry = Entry(color_field, width=10)
        prio_entry.pack(side=LEFT)
        if default_prio is not None:
            prio_entry.insert(0, default_prio)

        edge_settings['colors'].append({
            'hex': color_entry,
            'prio': prio_entry
        })


    def add_color_button(self, master, edge_settings):
        """Add Plus Button to generate extra color fields

        Elements:
            - Button
        """
        plus_button = Button(
            master,
            text='+',
            command=lambda: self.add_color_field(master=master, edge_settings=edge_settings),
            justify=CENTER
        )
        plus_button.pack(side=BOTTOM)


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
