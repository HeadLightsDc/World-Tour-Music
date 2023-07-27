from config import *
from data.data_config import User
from views.window_register import Register

# background image
bg_login = ctk.CTkImage(Image.open("resources\\background\\login_bg.png"), size=(1920, 1080))

# window login
class Login(Secundary_window):
        def __init__(self, parent):
            super().__init__(parent)
            
            self.parent = parent
            
            # ========== background config ==========
            self.bg_panel.configure(image = bg_login)

            # ========== Creating widgets ==========          
            self.username_entry = Entry_theme_1(self, placeholder_text = "Ingrese su usuario")
            
            self.password_entry = Entry_theme_1(self, placeholder_text = "Ingrese su contraseña", show = "*")
            
            self.login_button = Button(self,
                                       border_color= "black", 
                                       bg_color="#262626",
                                       fg_color= "#fafafa",
                                       hover_color= "#FEDF01",
                                       text = "Iniciar Sesión",
                                       text_color="black",
                                       command = lambda: self.login(),
                                       )
            
            self.register_button = Button(self,
                                          width=250,
                                          border_color="black",
                                          bg_color="black",
                                          fg_color="black",
                                          hover_color="#FEDF01",
                                          text = "Registrarse",
                                          command = lambda: self.open_register_window(),
                                          )
            
            self.incorrect_label_text = Label_text(self,
                                                   bg_color="black",
                                                   text = "El usuario o contraseña es incorrecto. Por favor intente de nuevo.",
                                                   size=12, 
                                                   text_color="red")
            
            # ========== Placing widgets ==========
            self.username_entry.place(x=1250, y=310)
            self.password_entry.place(x=1250, y=375)
            self.login_button.place(x=1250, y=440)
            self.register_button.place(x=680, y=989)
                
        def login(self):# login necesita ser modificado / Bug, se debe pedir una introduccion minima de caracteres al usar .get()
            
            """Se obtiene de lo escrito de los widgets username y password (Entry) al presionar el boton login del programa, se hace una verificacion de coincidencia de
            clave y valor en el archivo de registros de los usuarios account.json.
            
            Se destruye la ventana de login y se muestra la principal(Menu)"""
            
            user = self.username_entry.get()
            password = sha256(self.password_entry.get().encode('utf-8')).hexdigest()
            
            with open("data/account.json", "r") as file:
                data = json.load(file)
            
            user_list = data.get("users", [])
            
            for user_data in user_list:
                if user_data["user_id"] == user and user_data["password"] == password:
                    print("Inicio de Sesión ¡Exitoso!")
                    self.destroy()
                    self.parent.deiconify()
                    return
                else:
                    self.incorrect_label_text.place(x=1180, y=480)
                    self.username_entry.delete(0, "end")
                    self.password_entry.delete(0, "end")
                    self.login_button.focus()
                    
        def open_register_window(self):
            print("Ir a ventana de registro")
            window_register = Register(self)
            self.withdraw()
            window_register.wait_window()
            self.deiconify()
        
        