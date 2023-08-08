from config import *
from window_event import About_event
import tkintermapview

musical_route_bg = ctk.CTkImage(Image.open("resources\\background\\musical_route_bg.png"), size=(1920, 1080))

class Musical_route(Secundary_window):
    def __init__(self, parent, user_id):
        super().__init__(parent)
        
        self.bg_panel.configure(self, image = musical_route_bg)
        self.user_id = user_id
        # ========== map view widget========== 
        self.map_frame = ctk.CTkFrame(self, width=1283, height=882)
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=1283, height=882)
        self.map_widget.set_position(-24.7962783, -65.4150933) #Controla la ubicación por defecto del mapa
        self.map_widget.set_zoom(14) #Distancia de visualización del mapa
        
        self.map_frame.place(x=533, y=194)
        self.map_widget.place(x=0, y=0)
        
        # ========== frame event  ========== 
        self.eventmark_scrollable_frame = ctk.CTkScrollableFrame(self,
                                                                 corner_radius=0,
                                                                 border_width=0,
                                                                 width=411,
                                                                 height=883,
                                                                 fg_color= "#2B4257")
        
        self.eventmark_scrollable_frame.place(x=103, y=193)
        # ========== button widgets ==========
        self.back_window_button = Button(self,
                                         width = 150, 
                                         fg_color = "#BC1823",
                                         hover_color = "#369694",
                                         border_color = "black",
                                         text="Volver atras",
                                         command=lambda: self.back_window())
        
        self.back_window_button.place(x=1650, y=1030)
    
        # ========== inicializacion ==========
        self.load_events()
        
    def load_events(self, update=0):
        if update == 1:
            for widget in self.eventmark_scrollable_frame.winfo_children():
                widget.destroy()
        
        with open("data/account.json", "r") as file:
            data = json.load(file)
           
        user = data["account"].get(str(self.user_id))
        event_ids = user.get("event_history")
        
        with open("data/event.json", "r") as file:
            event_data = json.load(file)
        
        row = 0
        
        for event_id in event_ids:
            event = event_data["events"].get(event_id)
            if event:
                print(row)
                venue = event.get("venue")
                name = event.get("name")
                latitude = event.get("latitude")
                longitude = event.get("longitude")
                self.map_widget.set_marker(latitude, longitude, venue)
                
                set_map_button = Button_theme_1(self.eventmark_scrollable_frame, 
                                   width=310,
                                   size=15,
                                   text=name,
                                   command = lambda latitude=latitude, longitude=longitude: self.map_widget.set_position(latitude, longitude))

                set_map_button.grid(row=row, column=0, pady=10)

                event_button = Button_theme_1(self.eventmark_scrollable_frame,
                                              width=100,
                                              size=15,
                                              text="Detalle",
                                              command = lambda event_id = event_id: self.open_event_details_window(event_id))
                
                event_button.grid(row=row, column=1, pady=10)
                
                row += 1
    
    def open_event_details_window(self, event_id):
        
        """Mustra mas información sobre el evento seleccionado por el usuario"""
        
        print(f"Saber más sobre el evento con ID {event_id}")
        window_about_event = About_event(self, event_id, self.user_id, route_musical=True)
        self.withdraw()
        window_about_event.wait_window()
        self.deiconify()
        
    def back_window(self):
        
        """ Se autodestruye el objeto, cuando se destruye muestra el menu"""
        
        print("Cerrando ventana de añadir evento, volviendo a menu")
        self.destroy()
        