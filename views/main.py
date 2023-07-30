from window_menu import*
from window_login import Login

if __name__ == "__main__":
    
    # ========== Main Window ==========
    root = Menu()
    root.iconify()
    print("Menu Minimizado")
    
    # ========== Secundary Window - Login ==========
    window_login = Login(root)
    window_login.deiconify()
    
    root.mainloop()