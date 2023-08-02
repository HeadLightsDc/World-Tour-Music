from config import *
from data_config import Event
import tkintermapview

about_event_bg = ctk.CTkImage(Image.open("resources\\background\\about_event.png"), size=(1920, 1080))

class About_event(Secundary_window):
    def __init__(self, parent, event_id):
        super().__init__(parent)
        
        self.event_id = event_id
        self.bg_panel.configure(self, image = about_event_bg)
        
        # ========== Creating widgets ==========  
        self.venue_label = Label_text(self, size=40, fg_color="#F2F1EC", text_color="#BC1823")
        
        self.name_event_label = Label_text(self, size=35, fg_color="#F2F1EC")
        
        self.description_textbox = TextBox(self,          #Ver que hacer aqui...
                                           width=1680,
                                           height=150)
        
        self.address_label = Label_text(self, size=20, fg_color="#F2F1EC")
        
        self.date_label = Label_text(self, size=20, fg_color="#F2F1EC")
        
        self.schedule_label = Label_text(self, size=20, fg_color="#F2F1EC")
        
        self.add_event_button = Button_theme_1(self,
                                               text="Añadir evento",
                                               command=lambda: self.add_event(), ###Modificar
                                               )
        
        self.back_window_button = Button_theme_1(self, 
                                                 text="Volver atras",
                                                 command=lambda: self.back_window(),
                                                 )
        # ========== Map view Widget ==========
        self.map_widget = tkintermapview.TkinterMapView(self, 
                                                        width=1283, 
                                                        height=693, 
                                                        )
        
        # ========== Placing widgets ==========
        self.venue_label.place(x=120, y=83)
        self.name_event_label.place(x=770, y=148)
        
        
        self.description_textbox.place(x=120, y=210)
        self.address_label.place(x=120, y=445)
        self.date_label.place(x=120, y=620)
        self.schedule_label.place(x=120, y=800)
        self.add_event_button.place(x=170, y=945)
        self.back_window_button.place(x=170, y=1010)
        self.map_widget.place(x=533, y=383)
        
        # ========== Inicialización ==========
        self.event_detail_upload(event_id)
        
    def back_window(self):
        print("Cerrando ventana de añadir evento, volviendo a menu")
        self.destroy()
        
    def event_detail_upload(self, event_id):
        with open("data/event.json", "r") as file:
            data = json.load(file)
        
        evento = data["events"].get(str(event_id))
        
        venue = evento.get("venue")
        name = evento.get("name")
        description = evento.get("description")
        address = evento.get("address")
        latitude = evento.get("latitude")
        longitude = evento.get("longitude")
        date = evento.get("date")
        schedule = evento.get("schedule")
        
        self.venue_label.configure(text=venue)
        self.name_event_label.configure(text=name)
        self.address_label.configure(text=address)
        self.date_label.configure(text=date)
        self.schedule_label.configure(text=schedule)     
        
class Create_event(Secundary_window):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.bg_panel.configure(self, image = about_event_bg)
        self.last_event_id = self.get_last_id()
        self.events = {}
        
        # ========== Creating widgets ==========  
        self.venue_entry = Entry_theme_1(self, 
                                         width=620,
                                         placeholder_text="Estadio... Teatro... Centro de...",
                                         )
        
        self.name_event_entry = Entry_theme_1(self, width=1025,
                                              placeholder_text="Nombre del evento...")
        
        self.description_textbox = TextBox(self,
                                           width=1680,
                                           height=150,
                                           )
        
        self.address_entry = Entry_theme_1(self, 
                                           width=390,
                                           placeholder_text="Dirección...",
                                           )
        
        self.latitude_entry = Entry_theme_1(self, 
                                            width=185,
                                            placeholder_text="Latitud...",
                                            )
        
        self.longitude_entry = Entry_theme_1(self,
                                             width=185,
                                             placeholder_text="Longitud...",
                                             )
        
        self.date_entry = Entry_theme_1(self,
                                        width=390,
                                        placeholder_text="DD/MM/AA",
                                        )
        
        self.schedule_entry = Entry_theme_1(self, 
                                         width=390,
                                         placeholder_text="gs 20:00 a hs 00:00...",
                                         )
        
        self.error_label_text = Label_text(self,
                                           bg_color="#F2F1EC",
                                           text="Complete todos los campos requeridos.",
                                           size=12, 
                                           text_color="red",
                                           )
        
        self.add_event_button = Button_theme_1(self,
                                               text="Añadir evento",
                                               command=lambda: self.add_event(),
                                               )
        
        self.back_window_button = Button_theme_1(self, 
                                                 text="Volver atras",
                                                 command=lambda: self.back_window(),
                                                 )
        # ========== Map view Widget ==========
        self.map_widget = tkintermapview.TkinterMapView(self, 
                                                        width=1283, 
                                                        height=693, 
                                                        )
        
        # ========== Placing widgets ==========
        self.venue_entry.place(x=120, y=90)
        self.name_event_entry.place(x=770, y=150)
        self.description_textbox.place(x=120, y=210)
        self.address_entry.place(x=120, y=445)
        self.latitude_entry.place(x=120, y=495)
        self.longitude_entry.place(x=325, y=495)
        self.date_entry.place(x=120, y=620)
        self.schedule_entry.place(x=120, y=800)
        self.add_event_button.place(x=170, y=945)
        self.back_window_button.place(x=170, y=1010)
        self.map_widget.place(x=533, y=383)
        
    def back_window(self):
        print("Cerrando ventana de añadir evento, volviendo a menu")
        self.destroy()
        
    def add_event(self):
        venue = self.venue_entry.get()
        name = self.name_event_entry.get()
        description = self.description_textbox.get("1.0", "end")
        address = self.address_entry.get()
        latitude = self.latitude_entry.get()
        longitude = self.longitude_entry.get()
        date = self.date_entry.get()
        schedule = self.schedule_entry.get()
        
        if len(venue) == 0 or len(name) == 0 or len(description) == 0 or len(address) == 0 or len(latitude) == 0 or len(longitude) == 0 or len(date) == 0 or len(schedule) == 0:
            self.error_label_text.place(x=185, y=915)
            return
        
        new_event = Event(venue, name, description, address, latitude, longitude, date, schedule)

        self.last_event_id += 1
        new_event_id = self.last_event_id

        with open("data/event.json", "r") as file:
            data = json.load(file)

        if "events" not in data:
            data["events"] = {}

        data["events"][str(new_event_id)] = new_event.__dict__

        with open("data/event.json", "w") as file:
            json.dump(data, file, indent=4)
            
        print("Evento creado con exito!")
        print("Cerrando ventana de añadir evento, volviendo a menu")   
            
        return self.destroy()
            
    def get_last_id(self):
        with open("data/event.json", "r") as file:
            data = json.load(file)
            if data and "events" in data:
                events = data["events"]
                if events:
                    return max(int(event_id) for event_id in events.keys())
        return 0
    