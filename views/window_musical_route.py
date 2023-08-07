from config import *
import tkintermapview

musical_route_bg = ctk.CTkImage(Image.open("resources\\background\\musical_route_bg.png"), size=(1920, 1080))

class Musical_route(Secundary_window):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.bg_panel.configure(self, image = musical_route_bg)
        
        # ========== map view widget========== 
        self.map_frame = ctk.CTkFrame(self, width=1283, height=882)
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=1283, height=882)
        self.map_widget.set_zoom(16) #Distancia de visualización del mapa
        
        self.map_frame.place(x=533, y=194)
        self.map_widget.place(x=0, y=0)
        