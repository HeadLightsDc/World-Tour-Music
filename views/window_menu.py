from config import *
from window_event import Create_event, About_event

# background image
menu_bg = ctk.CTkImage(Image.open("resources\\background\\menu_bg.png"), size=(1920, 1080))

class Menu(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.admin = False
        print(self.admin)
            
        # ========== background config ==========      
        self.title("Tour World Music")
        self.attributes("-fullscreen", True)
        self.bg_panel = ctk.CTkLabel(self, text=None,
                                     image = menu_bg,
                                     )
    
        self.bg_panel.pack(fill="both", expand="yes")
        
        # ========== search widgets ==========
        self.eventmark_scrollable_frame = ctk.CTkScrollableFrame(self,
                                                                 corner_radius=0,
                                                                 border_width=0,
                                                                 width=1260,
                                                                 height=895,
                                                                 fg_color= "#F2F1EC")
        
        self.search_entry = Entry_theme_1(self,
                                        width=600,
                                        placeholder_text="Busqueda",
                                        size=16)
        
        self.eventmark_scrollable_frame.place(x=540, y=180)   
        self.search_entry.place(x=720, y=135)
        
        # ========== filter widgets ==========   
        self.filter1_checkbox = Checkbox_filter(self, text = "Teatro Provincial de Salta")
        
        self.filter2_checkbox = Checkbox_filter(self, text = "Centro de Convenciones")
        
        self.filter3_checkbox = Checkbox_filter(self, text = "Casa de la Cultura")
        
        self.filter4_checkbox = Checkbox_filter(self, text = "Estadio Delmi")
        
        self.filter_morning_checkbox = Checkbox_filter(self, text = "Mañana")
        
        self.filter_afternoon_checkbox = Checkbox_filter(self, text = "Tarde")
        
        self.filter_evening_checkbox = Checkbox_filter(self, text = "Noche")
            
        self.filter_morning_checkbox.place(x=150, y=330)
        self.filter_afternoon_checkbox.place(x=150, y=365)
        self.filter_evening_checkbox.place(x=150, y=400)
        
        self.filter1_checkbox.place(x=150, y=490)
        self.filter2_checkbox.place(x=150, y=525)
        self.filter3_checkbox.place(x=150, y=560)
        self.filter4_checkbox.place(x=150, y=595)
        
        # ========== Inicialización ==========
        self.show_event_widgets(0)  
    
    def admin_mode(self):
        
        """Este metodo se ejecuta unicamente en el login si el usuario es el Administrador crea dos botones, añadir eventos y eliminar eventos"""
        
        self.add_event_buttom = Button_theme_1(self,
                                               width = 145,
                                               text = "Añadir",
                                               command = lambda: self.open_create_event_window())
                
        self.delete_event_buttom = Button_theme_1(self, width = 145, text = "Eliminar")
                
        self.add_event_buttom.place(x=850, y=30)
        self.delete_event_buttom.place(x=850, y=70)
                
    def open_create_event_window(self):
        
        """Al hacer click en el boton(añadir evento) exclusivo de administrador se abre una ventana para añadir eventos"""
        
        print("Ir a ventana de añadir evento")
        window_create_event = Create_event(self)
        self.withdraw()
        window_create_event.wait_window()
        self.show_event_widgets(0) ###Checkear que pasa si le doy el parametro 1
        self.deiconify()
        
    def show_event_widgets(self, update = 0):
        
        """Este metodo, se inicializa automaticamente al crear un objeto con esta clase, el parametro update sirve para actualizar los eventos
        unicamente en el modo administrador """
        
        if update == 1:
            for widget in self.eventmark_scrollable_frame.winfo_children():
                widget.destroy()

        with open("data/event.json", "r") as file:
            data = json.load(file)

        if "events" in data:
            events = data["events"]
            for row, (event_id, event_data) in enumerate(events.items(), start=1):
                event_name = event_data["name"]
                
                label = Label_text(self.eventmark_scrollable_frame, 
                                   width=1035,
                                   text=event_name)
                
                label.grid(row=row, column=0, padx=20, pady=10)

                event_button = Button_theme_1(self.eventmark_scrollable_frame,
                                              width=175,
                                              text="Saber más",
                                              command=lambda event_id=event_id: self.open_event_details_window(event_id)
                                              )
                event_button.grid(row=row, column=1, pady=10)
                
    def open_event_details_window(self, event_id):
        
        """Mustra mas información sobre el evento seleccionado por el usuario"""
        
        print(f"Saber más sobre el evento con ID {event_id}")
        window_about_event = About_event(self, event_id)
        self.withdraw()
        window_about_event.wait_window()
        self.deiconify()