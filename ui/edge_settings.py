from tkinter import *


class EdgeSettings():
    def __init__(self, parent):
        self.parent = parent
    
        self.edge_group = LabelFrame(parent, text="Edges", padx=5, pady=5)
        self.edge_group.pack()

        self.edges = []

        self.generate_edge_color_group()

        self.add_edge_button(parent=self.edge_group)
    

    def generate_edge_color_group(self):
        parent = self.edge_group

        edge_color_group = LabelFrame(parent, text = 'Edge Colors', padx=5, pady=5)
        edge_color_group.pack()

        edge_settings = {
            'side': None,
            'width': None,
            'colors': []
        }

        self.edges.append(edge_settings)

        self.generate_side_field(parent=edge_color_group, settings=edge_settings)
        self.generate_width_field(parent=edge_color_group, settings=edge_settings)
        self.generate_color_field(parent=edge_color_group, settings=edge_settings)

        self.add_color_button(parent=edge_color_group, settings=edge_settings)


    def generate_side_field(self, parent, settings):
        Label(parent, text='Side').pack()
        side_entry = Entry(parent, width=30)
        side_entry.pack()
        side_entry.insert(0, 'top')

        settings['side'] = side_entry        


    def generate_width_field(self, parent, settings):
        Label(parent, text='Width').pack()
        width_entry = Entry(parent, width=30)
        width_entry.pack()
        width_entry.insert(0, '2')

        settings['width'] = width_entry


    def generate_color_field(self, parent, settings):
        color_field = Frame(parent)
        color_field.pack()

        Label(color_field, text='Hex').pack(side=LEFT)
        color_entry = Entry(color_field, width=20)
        color_entry.pack(side=LEFT)

        Label(color_field, text='Prio').pack(side=LEFT)
        prio_entry = Entry(color_field, width=10)
        prio_entry.pack(side=LEFT)

        settings['colors'].append({
            'hex': color_entry,
            'prio': prio_entry
        })
    

    def add_color_button(self, parent, settings):
        plus_button = Button(
            parent,
            text='+',
            command=lambda: self.generate_color_field(parent=parent, settings=settings),
            justify=CENTER
        )
        plus_button.pack(side=BOTTOM)

    
    def add_edge_button(self, parent):
        plus_button = Button(parent, text='+', command=self.generate_edge_color_group, justify=CENTER)
        plus_button.pack(side=BOTTOM)




          

