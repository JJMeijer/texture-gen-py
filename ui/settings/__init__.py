from tkinter import Frame, RIGHT

from .core_settings import CoreSettings
from .size_settings import SizeSettings
from .edge_settings import EdgeSettings

class Settings():
    def __init__(self, parent):
        self.parent = parent

        self.settings_frame = Frame(parent)
        self.settings_frame.pack(side=RIGHT)

        self.size_settings = SizeSettings(self.settings_frame)
        self.core_settings = CoreSettings(self.settings_frame)
        self.edge_settings = EdgeSettings(self.settings_frame)
