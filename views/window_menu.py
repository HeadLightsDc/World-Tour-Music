from config import *

# background image
menu_bg = ctk.CTkImage(Image.open("resources\\background\\menu_bg.png"), size=(1920, 1080))

class Menu(ctk.CTk):
    def __init__(self):
        super().__init__()
            
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
                                        height=45,
                                        size=20
                                        )
        
        self.filtered_frame = ctk.CTkFrame(self,
                                           width=311,
                                           height=792,
                                           fg_color= "#FEDF01"
                                           )
        
        self.eventmark_scrollable_frame = ctk.CTkScrollableFrame(self,
                                                                 width=1377,
                                                                 height=780,
                                                                 fg_color= "#FEDF01",
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
        self.search_entry.place(x=790, y=228)
        self.filtered_frame.place(x=103, y=288)
        self.eventmark_scrollable_frame.place(x=417, y=288)
        
        # ========== Frame filter ==========
        self.ubication_label_text.place(x=10, y=10)  
        self.filter_salta_checkbox.place(x=50, y=60)
        self.filter_bs_as_checkbox.place(x=50, y=95)
        self.filter_santa_fe_checkbox.place(x=50, y=130)
        
        self.schedule_label_text.place(x=10, y=165)
        self.filter_morning_checkbox.place(x=50, y=215)
        self.filter_afternoon_checkbox.place(x=50, y=250)
        self.filter_evening_checkbox.place(x=50, y=285)