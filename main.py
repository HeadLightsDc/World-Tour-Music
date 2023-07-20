import customtkinter as ctk
import json
from PIL import Image, ImageTk #Capaz no lo use ImageTk
from customtkinter import CTkFrame #Capaz no lo use
from hashlib import sha256

ctk.set_appearance_mode("dark")  # modos: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # temas: blue (default), dark-blue, green

# imagenes Png
button_search_icon = ctk.CTkImage(Image.open("resources\\icons\\search_logo.png"), size=(30, 30))
program_logo_icon = ctk.CTkImage(Image.open("resources\\icons\\program_logo.png"), size=(323, 58))
bg_login_png = ctk.CTkImage(Image.open("resources\\background\\background_login.png"), size=(1920, 1080))

# window login
class Login(ctk.CTk):
        def __init__(self):
            super().__init__()
            
            # ========== window config==========
            self.title("Proyecto Final")
            self.attributes("-fullscreen", True)
            
            # ========== background image ==========
            self.bg_panel = ctk.CTkLabel(self,
                                         text = None,
                                         image = bg_login_png)
            
            self.bg_panel.pack(fill="both", expand = "yes")
            
            # ========== login ==========
            #Creating widgets          
            self.username_entry = ctk.CTkEntry(self,
                                               width = 300,
                                               height= 35,
                                               corner_radius=5,
                                               border_width=2,
                                               border_color="white",
                                               bg_color="#262626",
                                               fg_color="black",
                                               text_color="white",
                                               placeholder_text ="Ingrese su usuario",
                                               placeholder_text_color="#dcdcdc",
                                               font = ("Open Sans", 16, "bold")
                                               )
            
            self.password_entry = ctk.CTkEntry(self,
                                               width = 300,
                                               height= 35,
                                               corner_radius=5,
                                               border_width=2,
                                               border_color= "white",
                                               bg_color="#262626",
                                               fg_color= "black",
                                               text_color="white",
                                               placeholder_text = "Ingrese su contraseña",
                                               placeholder_text_color="#dcdcdc",
                                               font = ("Open Sans", 16, "bold")
                                               )
            
            self.login_button = ctk.CTkButton(self,
                                              width = 300,
                                              height= 35,
                                              corner_radius=5,
                                              border_width=2,
                                              border_color= "black", 
                                              bg_color="#262626",
                                              fg_color= "#fafafa",
                                              hover_color= "#eeca06",
                                              text = "Iniciar Sesión",
                                              font = ("Open Sans", 16, "bold"),
                                              text_color="black",
                                              command = lambda: self.login(),
                                              )
            
            self.register_button = ctk.CTkButton(self,
                                                 width=200,
                                                 height=35,
                                                 corner_radius=5,
                                                 border_width=2,
                                                 border_color="black",
                                                 bg_color="black",
                                                 fg_color="black",
                                                 hover_color="#eeca06",
                                                 text = "Registrarse",
                                                 font = ("Open Sans", 16, "bold"),
                                                 command = lambda: self.register()
                                                 )
            
            #Placing widgets
            self.username_entry.place(x=1220, y=225)
            self.password_entry.place(x=1220, y=290)
            self.login_button.place(x=1220, y=355)
            self.register_button.place(x=645, y=991)
            
        def register(self): # register necesita ser modificado / Bug, se debe pedir una introduccion minima de caracteres al usar .get()
            
            """Se obtiene de lo escrito de los widgets username y password (Entry) al presionar el boton register del programa, se abre
            el archivo json que esta formateado en dict para que almacene el registro de los usuarios, este es actualizado con nueva data account = {user:password}
            """
            user = self.username_entry.get()
            password = sha256(self.password_entry.get().encode('utf-8')).hexdigest() # La contraseña es cifrado en SHA256 para luego validarla en el json
            
            with open("data\\account.json", "r") as file:
                data = json.load(file)
            account = {user:password}
            data.update(account)
            with open("data\\account.json", "w") as file:
                json.dump(data, file)
        
        def login(self): # login necesita ser modificado / Bug, se debe pedir una introduccion minima de caracteres al usar .get()
            
            """Se obtiene de lo escrito de los widgets username y password (Entry) al presionar el boton login del programa, se hace una verificacion de coincidencia de
            clave y valor en el archivo de registros de los usuarios account.json. En caso de estar registrado se notificara al usuario y viceversa """
            
            user = self.username_entry.get()
            password = sha256(self.password_entry.get().encode('utf-8')).hexdigest() # La contraseña es cifrado en SHA256 para luego validarla en el json
            
            with open("data\\account.json", "r") as file:
                data = json.load(file)
            
            if any(u == user and p == password for u, p in data.items()):
                print("Inicio de sesión correctamente")
            else:
                print("No estás registrado")
                
app = Login()
app.mainloop()