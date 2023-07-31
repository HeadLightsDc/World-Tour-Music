import customtkinter as ctk
from customtkinter import CTkFrame
from PIL import Image
import json
import re
from hashlib import sha256

ctk.set_appearance_mode("dark")  # modos: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # temas: blue (default), dark-blue, green


class Secundary_window(ctk.CTkToplevel):
    
    """Configuración basica para todas las ventanas secundarias"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
         # ========== background config ==========      
        self.title("Proyecto Final")
        self.attributes("-fullscreen", True)
        self.bg_panel = ctk.CTkLabel(self, text=None)
        
        # ========== placing background ==========
        self.bg_panel.pack(fill="both", expand="yes")

class Entry(ctk.CTkEntry):
    
    """ Configuración de Widget Entry """
    
    def __init__(self, *args, width=300, height = 35, corner_radius = 5, border_width=2, size = 16, **kwargs):  #Aquí, el constructor de la clase actual (self) acepta argumentos variables (args y kwargs).
        super().__init__(*args, **kwargs)                                    #Luego, se pasa todo el conjunto de argumentos (args y kwargs) a través de la llamada a 
        self.configure(                                                      #super().__init__(*args, **kwargs). Esto significa que cualquier argumento que se pase al
            width = width,                                                   #constructor de la clase actual se transmitirá al constructor de la clase base.
            height = height,                                                 #  ¡Esto permite flexibilidad!
            corner_radius = corner_radius,
            border_width = border_width,
            placeholder_text_color = "#dcdcdc",
            font = ("Open Sans", size, "bold"),
            )
        
class Entry_theme_1(Entry):
    
    """ Tema de colores para Widget Entry """
    
    def __init__(self,*args, border_color = "white", bg_color = "#262626", fg_color = "black", text_color = "white", **kwargs):
        super().__init__(*args, **kwargs)                                                                                      
        self.configure(
            border_color = border_color,
            corner_radius = 0,
            bg_color = bg_color,                                                                   
            fg_color = fg_color,
            text_color = text_color,
            )       
        
class Button(ctk.CTkButton):
    
    """ Configuración de Widget Button """
    
    def __init__(self, *args, width=300, height=35, corner_radius=5, border_width=2, size=16, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(
            width=width,
            height=height, 
            corner_radius=corner_radius,
            border_width=border_width,
            font=("Open Sans", size, "bold"),
            ) 
        
class Button_theme_1(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(border_color="black",
                       fg_color="white",
                       hover_color="#84DCCF",
                       text_color="black",
                       )       
        
class Checkbox_filter(ctk.CTkCheckBox):
    
    """ Configuración de Widget Checkbox """
    
    def __init__(self, *args, size=16,**kwargs):
        super().__init__(*args, **kwargs)
        self.configure(
            width=100,
            font=("Open Sans", size, "normal"),
            border_color="black",
            text_color="black",
            )       
        
class Label_text(ctk.CTkLabel):
    
    """ Configuración de Widget Label de texto """
    
    def __init__(self, *args, size=32, text_color="black",**kwargs):
        super().__init__(*args, **kwargs)
        self.configure(
            font=("Open Sans", size, "bold"),
            text_color=text_color,
            )
        
class TextBox(ctk.CTkTextbox):
    """ Configuración de Widget TextBox"""
    
    def __init__(self, *args, size=32, width, height, text_color="white",**kwargs):
        super().__init__(*args, **kwargs)
        self.configure(
            border_color = "white",
            fg_color = "black",
            border_width=2,
            corner_radius=0,
            width=width,
            height=height,
            font=("Open Sans", size, "bold"),
            text_color=text_color,
            )
    
    
                                              
                                               