from config import *
from data_config import Event
import tkintermapview

about_event_bg = ctk.CTkImage(Image.open("resources\\background\\about_event.png"), size=(1920, 1080))

class About_event(Secundary_window):
    def __init__(self, parent, event_id, select_ubication_callback=None):
        super().__init__(parent)
        
        self.bg_panel.configure(self, image = about_event_bg)
        
        # ========== variable ========== 
        self.event_id = event_id
        self.select_ubication_callback = select_ubication_callback
        
        # ========== title widgets ==========  
        self.venue_label = Label_text(self, width=747.5, size=40, fg_color="#2B4257", text_color="#369694", anchor="center")
        
        self.name_event_label = Label_text(self, size=35, fg_color="#369694", text_color="#2B4257")
        
        self.venue_label.place(x=104, y=130)
        self.name_event_label.place(x=865, y=148)
        
        # ========== about event widget ========== 
        self.description_label_text = Label_text(self,         
                                           width=1680,
                                           height=150,
                                           size=20, 
                                           fg_color="#F2F1EC",
                                           anchor="nw",
                                           justify="left")
        
        self.description_label_text.place(x=120, y=210)
        
        # ========== Location event widgets (map view)========== 
        self.address_label = Label_text(self, size=20, fg_color="#F2F1EC")
        
        self.map_frame = ctk.CTkFrame(self, width=1283, height=693)
        
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=1283, height=693)
        self.map_widget.set_zoom(16) #Distancia de visualización del mapa
        
        self.address_label.place(x=120, y=800)
        self.map_frame.place(x=533, y=383)
        self.map_widget.place(x=0, y=0)
        
        # ========== Date/time widgets ==========
        self.start_time_label = Label_text(self, size=20, fg_color="#F2F1EC")
        
        self.end_time_label = Label_text(self, size=20, fg_color="#F2F1EC")
        
        self.start_time_label.place(x=240, y=622)
        self.end_time_label.place(x=240, y=669)
        
        
        # ========== Buttom widgets ==========
        self.add_event_button = Button_theme_1(self,
                                               text="Añadir evento",
                                               command=lambda: self.add_event()) ###Modificar
        
        self.back_window_button = Button_theme_1(self, 
                                                 text="Volver atras",
                                                 command=lambda: self.back_window())
        
        self.add_event_button.place(x=170, y=945)
        self.back_window_button.place(x=170, y=1010)
        
        # ========== Inicialización ==========
        self.event_detail_upload(event_id)
        
    def back_window(self):
        
        """ Se autodestruye el objeto, cuando se destruye muestra el menu"""
        
        print("Cerrando ventana de añadir evento, volviendo a menu")
        self.destroy()
        
    def event_detail_upload(self, event_id):
        
        """Carga de la informacion del evento seleccionado en el menu, hace uso de archivo json, necesita el id del evento"""
        
        with open("data/event.json", "r") as file:
            data = json.load(file)
        
        evento = data["events"].get(str(event_id))
        
        venue = evento.get("venue")
        name = evento.get("name")
        description = evento.get("description")
        address = evento.get("address")
        latitude = evento.get("latitude")
        longitude = evento.get("longitude")
        start_time = evento.get("start_time")
        end_time = evento.get("end_time")
        
        self.venue_label.configure(text=venue)
        self.name_event_label.configure(text=name)
        self.description_label_text.configure(text=description)
        self.address_label.configure(text=address)
        self.start_time_label.configure(text=start_time)
        self.end_time_label.configure(text=end_time)
        
        
        self.map_widget.set_position(latitude, longitude)
        self.add_marker_to_map(latitude, longitude, venue)
        
    def add_marker_to_map(self, latitud, longitud, texto, imagen=None):
        
        """Permite añadir una marca al mapa"""
        return self.map_widget.set_marker(latitud, longitud, text=texto, image=imagen, command=self.select_ubication_callback)     
        
class Create_event(Secundary_window):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.bg_panel.configure(self, image = about_event_bg)
        
        # ========== variable ==========
        self.last_event_id = self.get_last_id()
        self.events = {}
        
        # ========== map view widget ==========
        self.map_frame = ctk.CTkFrame(self, width=1283, height=693)
        self.map_frame.place(x=533, y=383)      
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=1283, height=693)
        self.map_widget.set_position(-24.7891876, -65.4103297) #Controla la ubicación por defecto del mapa
        self.map_widget.set_zoom(16) #Distancia de visualización del mapa
        
        self.map_widget.place(x=0, y=0)
        
        # ========== place, name and description widgets ==========  
        self.venue_entry = Entry_theme_1(self, 
                                         width=715,
                                         placeholder_text="Estadio... Teatro... Centro de...")
        
        self.name_event_entry = Entry_theme_1(self, width=755,
                                              placeholder_text="Nombre del evento...")
        
        self.description_textbox = TextBox(self,
                                           width=1680,
                                           height=150,
                                           size=20)
       
        self.venue_entry.place(x=120, y=150)
        self.name_event_entry.place(x=865, y=150)
        self.description_textbox.place(x=120, y=210)
        
        # ========== start Date/time widgets ==========  
        self.start_date_entry = DateEntry(self,
                                    background="#84dccf",
                                    locale = "es_AR",  
                                    width=8,
                                    foreground="#f2f1ec", 
                                    borderwidth=2,
                                    font=("Open Sans Extra Bold", 16, "bold"))
        
        self.start_hour_entry = Entry_theme_1(self, width=35, placeholder_text = "HH")
        self.start_hour_entry.configure(validate="key", validatecommand=(self.register(self.validate_hour), "%P"))
        
        self.start_minute_entry = Entry_theme_1(self, width=35, placeholder_text = "MM")
        self.start_minute_entry.configure(validate="key", validatecommand=(self.register(self.validate_minute), "%P"))
        
        self.start_date_entry.place(x=245, y=618)
        self.start_hour_entry.place(x=375, y=615)
        self.start_minute_entry.place(x=420, y=615)
        
        # ========== end Date/time widgets ==========
        self.end_date_entry = DateEntry(self,
                                    background="#84dccf",
                                    locale = "es_AR",  
                                    width=8,
                                    foreground="#f2f1ec", 
                                    borderwidth=2,
                                    font=("Open Sans Extra Bold", 16, "bold"))
        
        self.end_hour_entry = Entry_theme_1(self, width=35, placeholder_text = "HH")
        self.end_hour_entry.configure(validate="key", validatecommand=(self.register(self.validate_hour), "%P"))
        
        self.end_minute_entry = Entry_theme_1(self, width=35, placeholder_text = "MM")
        self.end_minute_entry.configure(validate="key", validatecommand=(self.register(self.validate_minute), "%P"))
        
        self.end_date_entry.place(x=245, y=666)
        self.end_hour_entry.place(x=375, y=663)
        self.end_minute_entry.place(x=420, y=663)
        
       # ========== Location widgets ========== 
        self.address_entry = Entry_theme_1(self, 
                                           width=390,
                                           placeholder_text="Dirección...")
        
        self.latitude_entry = Entry_theme_1(self, 
                                            width=185,
                                            placeholder_text="Latitud...")
        
        self.longitude_entry = Entry_theme_1(self,
                                             width=185,
                                             placeholder_text="Longitud...")

        self.address_entry.place(x=120, y=800)
        self.latitude_entry.place(x=120, y=850)
        self.longitude_entry.place(x=325, y=850)
        
        
        # ========== Button widgets and label error widget ==========  
        self.error_label_text = Label_text(self,
                                           bg_color="#F2F1EC",
                                           text="Complete todos los campos requeridos.",
                                           size=12, 
                                           text_color="red")
        
        self.add_event_button = Button_theme_1(self,
                                               text="Añadir evento",
                                               command=lambda: self.add_event())
        
        self.back_window_button = Button_theme_1(self, 
                                                 text="Volver atras",
                                                 command=lambda: self.back_window())
        
        self.add_event_button.place(x=170, y=945)
        self.back_window_button.place(x=170, y=1010)
        
    def back_window(self):
        
        """ Se autodestruye el objeto, cuando se destruye muestra el menu"""
        
        print("Cerrando ventana de añadir evento, volviendo a menu")
        self.destroy()
        
    def add_event(self):
        
        """Obtiene de todos los widgets de ingreso de datos al hacer click añadir evento, se verifica si estos son correctos
        se crea un objeto Event con esos datos y se guardan con un nuevo id en el json"""
        
        venue = self.venue_entry.get()
        name = self.name_event_entry.get()
        description = self.description_textbox.get("1.0", "end")
        address = self.address_entry.get()
        latitude = float(self.latitude_entry.get()) #SI ESTA VACIO CAUSA UN ERROR EVITARLO EN LA INTEGRACION DE CLICK EN EL MAPA
        longitude = float(self.longitude_entry.get()) #SI ESTA VACIO CAUSA UN ERROR EVITARLO EN LA INTEGRACION DE CLICK EN EL MAPA
        start_hour = self.start_hour_entry.get()
        start_minute = self.start_minute_entry.get()
        end_hour = self.end_hour_entry.get()
        end_minute = self.end_minute_entry.get()

        start_date = self.start_date_entry.get_date() #Se obtiene la fecha en formato ISO ISO 8601
        start_date_str = start_date.isoformat() #retorna un string que representa la hora en formato ISO 8601
        
        end_date = self.end_date_entry.get_date() #Se obtiene la fecha en formato ISO ISO 8601
        end_date_str = end_date.isoformat() #retorna un string que representa la hora en formato ISO 8601

        
        if len(venue) == 0 or len(name) == 0 or len(description) == 0 or len(address) == 0 or latitude == None or longitude == 0 or len(start_hour) == 0 or len(start_minute) == 0 or len(end_hour) == 0 or len(end_minute) == 0:
            self.error_label_text.place(x=185, y=915)                                   #None no actua como lo esperado...
            return
        
        start_time = f"{start_date_str} a las {start_hour}:{start_minute}"                               
        end_time = f"{end_date_str} a las {end_hour}:{end_minute}"
        
        new_event = Event(venue, name, description, address, latitude, longitude, start_time, end_time)

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
            
        return self.back_window()
            
    def get_last_id(self):
        
        """Obtiene el ultimo ID de los eventos que estan en el json"""
        
        with open("data/event.json", "r") as file:
            data = json.load(file)
            if data and "events" in data:
                events = data["events"]
                if events:
                    return max(int(event_id) for event_id in events.keys())
        return 0
    
    def validate_hour(self, input_value):
        
        """No permite que se ingresen letras y caracteres especiales en un widget entry se utiliza
        para permitir la entrada de un rango de hora correcto"""
        
        if input_value.strip() == "":
            return True
        try:
            hour = int(input_value)
            return 0 <= hour <= 23 and len(input_value) <= 2
        except ValueError:
            return False

    def validate_minute(self, input_value):
        """No permite que se ingresen letras y caracteres especiales en un widget entry se utiliza
        para permitir la entrada de un rango de minuto correcto"""
        
        if input_value.strip() == "":
            return True
        try:
            minute = int(input_value)
            return 0 <= minute <= 59 and len(input_value) <= 2
        except ValueError:
            return False