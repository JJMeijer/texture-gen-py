from tkinter import *


class CoreSettings():
    def __init__(self, parent):
        self.parent = parent
    
        self.color_group = LabelFrame(parent, text="Core Colors", padx=5, pady=5)
        self.color_group.pack()

        self.colors = []

        self.generate_color_field()
        
        self.add_plus_button()
    

    def generate_color_field(self):
        master = self.color_group
        

        color_field = Frame(master)
        color_field.pack()

        Label(master=color_field, text='Hex').pack(side=LEFT)
        color_entry = Entry(master=color_field, width=20)
        color_entry.pack(side=LEFT)

        Label(master=color_field, text='Prio').pack(side=LEFT)
        prio_entry = Entry(master=color_field, width=10)
        prio_entry.pack(side=LEFT)

        self.colors.append({
            'hex': color_entry,
            'prio': prio_entry
        })
    
    def add_plus_button(self):
        plus_button = Button(master=self.color_group, text='+', command=self.generate_color_field, justify=CENTER)
        plus_button.pack(side=BOTTOM)




          

