from config import *
from data.data_config import User

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
            
            self.register_button = Button(self,
                                          width=200,
                                          border_color="black",
                                          bg_color="black",
                                          fg_color="black",
                                          hover_color="#FEDF01",
                                          text = "Registrarse",
                                          command = lambda: self.register(),
                                          )
            
            # ========== Placing widgets ==========  
            self.name_entry.place(x=810, y=416)
            self.lastname_entry.place(x=810, y=503)
            self.email_entry.place(x=810, y=589)
            self.username_entry.place(x=810, y=675)
            self.password_entry.place(x=810, y=761)
            
            self.register_button.place(x=860, y = 840)


        def register(self):
            
            name = self.name_entry.get()
            lastname = self.lastname_entry.get()
            email = self.email_entry.get()
            user = self.username_entry.get()
            password = sha256(self.password_entry.get().encode('utf-8')).hexdigest()

            # Crear una instancia de User con los datos ingresados
            account = User(name, lastname, email, user, password)

            with open("data/account.json", "r") as file:
                data = json.load(file)
                
            # Obtener la lista actual de usuarios del archivo JSON o inicializarla si no existe
            user_list = data.get("users", [])
            
            if not data:
                data = {}
            
            # Convertir la instancia de User en un diccionario y agregarlo a la lista
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
            
            self.destroy()
            
            