from config import *
import tkintermapview

about_event_bg = ctk.CTkImage(Image.open("resources\\background\\about_event.png"), size=(1920, 1080))

class About_event(Secundary_window): #Despues de desarollar el diseño de la ventana hacerla Secundaria
    def __init__(self, parent): #Acordarese de poner parent en init y super
        super().__init__(parent)
        
        # ========== Creating widgets ==========  
        self.bg_panel.configure(self, image = about_event_bg)
        
        self.buy_button = Button_theme_1(self,text="Ir a comprar",)
        
        self.back_window_button = Button_theme_1(self, text="Volver atras")
        
        # ========== Map view Widget ==========
        self.map_widget = tkintermapview.TkinterMapView(self, 
                                                        width=1283, 
                                                        height=693, 
                                                        )
        
        
        # ========== Placing widgets ==========
        self.map_widget.place(x=533, y=383)
        self.buy_button.place(x=170, y=945)
        self.back_window_button.place(x=170, y=1020)