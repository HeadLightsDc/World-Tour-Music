from config import *
from window_event import Create_event

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
        
        # ========== placing background ==========
        self.bg_panel.pack(fill="both", expand="yes")
        
        # ========== Creating widgets ==========
        self.search_entry = Entry_theme_1(self,
                                        width=600,
                                        placeholder_text="Busqueda",
                                        size=16,
                                        )
        
        self.filtered_frame = ctk.CTkFrame(self,
                                           corner_radius=0,
                                           width=432,
                                           height=694,
                                           fg_color= "#F2F1EC"
                                           )
        
        self.eventmark_scrollable_frame = ctk.CTkScrollableFrame(self,
                                                                 corner_radius=0,
                                                                 border_width=0,
                                                                 width=1260,
                                                                 height=693,
                                                                 fg_color= "#F2F1EC",
                                                                 )
        
        # ========== frame filter widgets ==========  
        
        self.ubication_label_text = Label_text(self.filtered_frame,
                                               text= "Ubicación")
        
        self.filter_salta_checkbox = Checkbox_filter(self.filtered_frame,
                                                           text = "Salta")
        
        self.filter_bs_as_checkbox = Checkbox_filter(self.filtered_frame,
                                                           text = "Buenos Aires")
        
        self.filter_santa_fe_checkbox = Checkbox_filter(self.filtered_frame,
                                                           text = "Santa fe")
        
        
        self.schedule_label_text = Label_text(self.filtered_frame,
                                              text="Horario")
        
        self.filter_morning_checkbox = Checkbox_filter(self.filtered_frame,
                                                           text = "Hs: 7:00 a 12:00")
        
        self.filter_afternoon_checkbox = Checkbox_filter(self.filtered_frame,
                                                           text = "Hs: 13:00 a 18:00")
        
        self.filter_evening_checkbox = Checkbox_filter(self.filtered_frame,
                                                         text = "Hs: 19:00 a 00:00")
        
        # ========== Placing widgets ==========  
        self.search_entry.place(x=815, y=333.5)
        self.filtered_frame.place(x=103.5, y=382.4)
        self.eventmark_scrollable_frame.place(x=540, y=382.4)
        
        # ========== Frame filter ==========
        self.ubication_label_text.place(x=10, y=10)  
        self.filter_salta_checkbox.place(x=50, y=60)
        self.filter_bs_as_checkbox.place(x=50, y=95)
        self.filter_santa_fe_checkbox.place(x=50, y=130)
        
        self.schedule_label_text.place(x=10, y=165)
        self.filter_morning_checkbox.place(x=50, y=215)
        self.filter_afternoon_checkbox.place(x=50, y=250)
        self.filter_evening_checkbox.place(x=50, y=285)
    
    def admin_mode(self):
                self.add_event_buttom = Button_theme_1(self,
                                                       width = 145,
                                                       text = "Añadir",
                                                       command = lambda: self.open_create_event_window(),
                                                       )
                
                self.delete_event_buttom = Button_theme_1(self,
                                                          width = 145,
                                                          text = "Eliminar",
                                                          )
                
                self.add_event_buttom.place(x=1490, y=333.5)
                self.delete_event_buttom.place(x=1660, y=333.5)
                
    def open_create_event_window(self):
        print("Ir a ventana de añadir evento")
        window_create_event = Create_event(self)
        self.withdraw()
        window_create_event.wait_window()
        self.deiconify()