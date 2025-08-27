from tokenize import Double
import customtkinter


#
app = customtkinter.CTk()

def DefaultCALLBACK():
    print("button was clicked")
def Main_Window(Title, Size1, Size2):
    app.title(f"{Title}")
    app.geometry(f"{Size1}x{Size2}")

def Main_Window_Scaled(Title: str, Size: float):
    app.title(f"{Title}")
    customtkinter.set_window_scaling(Size)

def LightSwitch(Switch: bool):
    if Switch == True:
        customtkinter.set_appearance_mode("light")
    elif Switch == False:
        customtkinter.set_appearance_mode("dark")
    if Switch == None:
        customtkinter.set_appearance_mode("system")

def Theme(Color):
    if Color == "blue".strip():
        customtkinter.set_default_color_theme("blue")
    elif Color == "green".strip():
        customtkinter.set_default_color_theme("green")
    elif Color == "dark-blue".strip() or "darkblue".strip():
        customtkinter.set_default_color_theme("dark-blue")

def Custom_Theme(path):
    customtkinter.set_default_color_theme(path)
def New_Button(button_text, button_row, button_column, button_paddx, button_paddy, callback):
    New_button_Holder = customtkinter.CTkButton(app, text=button_text, command=callback)
    New_button_Holder.grid(row=button_row, column=button_column, padx=button_paddx, pady=button_paddy)

def New_CheckBox(Box_identity, Box_Text: str, Box_Row: int, Box_column: int, Box_Paddx: int, Box_paddy, *Box_Sticky: str, **Box_StickyCustom: bool):
    if Box_StickyCustom == True:
        Box_identity = customtkinter.CTkCheckBox(app, text=Box_Text)
        Box_identity.grid(row=Box_Row, column=Box_column, padx=Box_Paddx, pady=Box_paddy, sticky="w") #Default Sticky in docs
    elif Box_StickyCustom == False:
        Box_identity = customtkinter.CTkCheckBox(app, text=Box_Text)
        Box_identity.grid(row=Box_Row, column=Box_column, padx=Box_Paddx, pady=Box_paddy, sticky=f"{Box_Sticky}") # Custom Sticky (have yet to find out what sticky does august 26 2025)

def New_CheckBoxFrame():
    pass

def New_TextBox():
    customtkinter.CTkTextbox(app)

def TextboxInsert(line, message):
    pass



