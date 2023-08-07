from config import *
from window_register import Register

# background image
bg_login = ctk.CTkImage(Image.open("resources\\background\\login_bg.png"), size=(1920, 1080))

# window login
class Login(Secundary_window):
        def __init__(self, parent):
            super().__init__(parent)
            
            self.parent=parent
            
            # ========== background config ==========
            self.bg_panel.configure(image = bg_login)

            # ========== Creating widgets ==========          
            self.username_entry = Entry_theme_1(self, placeholder_text = "Ingrese su usuario")
            
            self.password_entry = Entry_theme_1(self, placeholder_text = "Ingrese su contraseña", show = "*")
            
            self.login_button = Button_theme_1(self,
                                               text = "Iniciar Sesión",
                                               text_color="black",
                                               command = lambda: self.login(),
                                               )
            
            self.register_button = Button_theme_1(self,
                                                  width=250,
                                                  text = "Registrarse",
                                                  command = lambda: self.open_register_window(),
                                                  )
            
            self.error_label_text = Label_text(self,
                                               bg_color="black",
                                               size=12, 
                                               text_color="red")
            
            # ========== Placing widgets ==========
            self.username_entry.place(x=1250, y=310)
            self.password_entry.place(x=1250, y=375)
            self.login_button.place(x=1250, y=440)
            self.register_button.place(x=680, y=989)
                
        def login(self):
            
            """El método permite iniciar sesión al usuario
            
            Se hace una entrada de datos (Usuario/Contraseña) por medio de los widgets, luegos se hace 
            una verificacion de coincidencia de clave y valor en el archivo de registros de los usuarios account.json.
            
            Se destruye la ventana de login y se muestra la principal(Menu)"""
            
            min_chars = 8
            error_min_chars = "Usuario y Contraseña deben contener un mínimo de 8 caracteres."
            error_incorrect = "El usuario o contraseña es incorrecto. Por favor intente de nuevo."
            
            user = self.username_entry.get()
            password = self.password_entry.get()
            
            if len(user) < min_chars or len(password) < min_chars:
                self.error_label_text.configure(text = error_min_chars)
                self.error()
                return
            
            password = sha256(password.encode('utf-8')).hexdigest()
            
            with open("data/account.json", "r") as file:
                data = json.load(file)
            
            user_data = data.get("account", {})
            
            for user_id, user_info in user_data.items():
                if user_info["nickname"] == user and user_info["password"] == password:
                    print("Inicio de Sesión ¡Exitoso!")
                    if user == "Administrador":
                        self.parent.admin_mode()
                        print("El usuario que inicio sesión es el administrador")
                    return self.destroy(), self.parent.deiconify()
                else:
                    self.error_label_text.configure(text = error_incorrect)
                    self.error()

            
        def error(self):
            self.error_label_text.place(x=1180, y=480)
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
            self.login_button.focus()
                  
                    
        def open_register_window(self):
            print("Ir a ventana de registro")
            window_register = Register(self)
            self.withdraw()
            window_register.wait_window()
            self.deiconify()
        