from config import *
from data_config import User

# background image
bg_register = ctk.CTkImage(Image.open("resources\\background\\register_bg.png"), size=(1920, 1080))

class Register(Secundary_window):
        def __init__(self, parent):
            super().__init__(parent)
            
            # ========== background config ==========
            self.bg_panel.configure(image = bg_register)
            
            # ========== Creating widgets ==========
            self.name_entry = Entry_theme_1(self)
            self.lastname_entry = Entry_theme_1(self)
            self.email_entry = Entry_theme_1(self)
            self.username_entry = Entry_theme_1(self)
            self.password_entry = Entry_theme_1(self)
            
            self.error_label_text = Label_text(self,
                                               bg_color="#84DCCF",
                                               size=12, 
                                               text_color="red")
            
            self.register_button = Button_theme_1(self,
                                          width=200,
                                          text = "Registrarse",
                                          command = lambda: self.register(),
                                          )
            
            # ========== Placing widgets ==========  
            self.name_entry.place(x=810, y=416)
            self.lastname_entry.place(x=810, y=503)
            self.email_entry.place(x=810, y=589)
            self.username_entry.place(x=810, y=675)
            self.password_entry.place(x=810, y=761)
            
            self.register_button.place(x=860, y=840)

        def register(self):
            
            """Este método permite al usuario registrarse
            
            Se hace una entrada de datos por medio de los widgets "Entry" posteriormente son validos y notifica al
            usuario si hubo un error con los datos introducidos. Si todo esta perfecto se añade la información a la
            base de datos (json)."""
            
            name = self.name_entry.get()
            lastname = self.lastname_entry.get()
            email = self.email_entry.get()
            user = self.username_entry.get()
            password = self.password_entry.get()
            
            error_message = self.check_data(name, lastname, email, user, password)
            if error_message:
                self.notification_error(error_message)
                return
            
            password = sha256(password.encode('utf-8')).hexdigest()
            # Creación de un objetos User con los datos ingresados como atributos
            account = User(name, lastname, email, user, password)

            with open("data/account.json", "r") as file:
                data = json.load(file)
                
            user_list = data.get("users", [])
            
            if not data:
                data = {}
            
            # Convierte el objeto User en un diccionario y se agrega a una lista
            user_list.append({
                "name": account.name,
                "lastname": account.lastname,
                "email": account.email,
                "user_id": account.user_id,
                "password": account.password,
                "event_history": account.event_history
                })
            
            # Actualizar el archivo JSON con la nueva lista de usuarios
            data["users"] = user_list
            
            with open("data/account.json", "w") as file:
                json.dump(data, file)
            
            print("Registrado con exito")
            
            return self.destroy()
            
        def check_data(self, name, lastname, email, user, password):
            
            "Valida los datos ingresados en el registro si todo esta bien se continua con el registro, sino se notifica el error cometido"
            
            min_chars = 8
            valid_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            valid_name_or_lastname = r'^[A-Z][a-z]*$'
            
            if len(name) == 0 or len(lastname) == 0 or len(email) == 0 or len(user) == 0 or len(password) == 0:
                error = "Para poder registrase complete los campos requeridos."
                return error
            
            if not (re.fullmatch(valid_name_or_lastname, name)):
                error = "No se permiten números y caracteres especiales en el nombre. Debe empezar con una letra en mayuscula."
                return error
            
            if not (re.fullmatch(valid_name_or_lastname, lastname)):
                error = "No se permiten números y caracteres especiales en el apellido. Debe empezar con una letra en mayuscula"
                return error
            
            if not (re.fullmatch(valid_email, email)):
                error = "El correo electronico ingresado no es valido."
                return error
            
            if len(user) < min_chars and len(password) < min_chars:
                error = "El usuario y contraseña deben contener como mínimo 8 caracteres."
                return error
            
            if len(user) < min_chars:
                error = "El usuario debe contener como mínimo 8 caracteres."
                return error
            
            if len(password) < min_chars:
                error = "La contraseña debe contener como mínimo 8 caracteres."
                return error 
            
        def notification_error(self, message):
            
            """Toma como argumento el error y muestra posteriormente en pantalla el error"""
            
            self.error_label_text.configure(text = message)
            self.error_label_text.place(x=800, y=810)