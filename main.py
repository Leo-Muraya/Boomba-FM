import customtkinter as ctk


#setting the appearance and the theme
ctk.set_appearance_mode ("dark")
ctk.set_default_color_theme("blue")

#main window
app = ctk.CTk()
app.title("Music Player")
app.geometry("1100x600")

#dividing the space in the window

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1,weight=1)
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight= 1)
app.grid_columnconfigure(2,weight=0)

#sidebar
sidebar = ctk.CTkFrame(master = app, width=180, fg_color = "#1a1a2e")
sidebar.grid(row=0 ,column =0 , sticky="nsew", padx= (10,5), pady=5)

#main area

main_area= ctk.CTkFrame(master= app, fg_color="#1a1a2e")
main_area.grid(row=0, column=1, sticky= "nsew",padx=5, pady=5)

#visualizer panel
visualizer=ctk.CTkFrame(master= app, width=220, fg_color= "#1a1a2e")
visualizer.grid(row=0 , column=2, sticky= "nsew",padx=5,pady=5)




#start the window
app.mainloop()