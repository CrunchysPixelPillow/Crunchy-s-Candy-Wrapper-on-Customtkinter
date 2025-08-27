  # Crunchy's Candy Wrapper on Customtkinter
  
  [![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
  [![Customtkinter](https://img.shields.io/badge/Customtkinter-v1.0-orange)](https://github.com/customtkinter)
  
  ## Description
  
  This repository contains the Crunchy's Candy Wrapper application built using Customtkinter in Python.
  
  ## Key Features and Highlights
  
  - Customized candy wrapper design
  - Interactive GUI using Customtkinter
  - Python-based application
  
  ## Installation
  
  To use Crunchy's Candy Wrapper, follow these steps:
  
  1. Clone the repository or Install release:
  
  ```bash
  git clone https://github.com/username/Crunchy-s-Candy-Wrapper-on-Customtkinter.git
  ```
  
  2. Install Customtkinter:
  
  ```bash
  pip install customtkinter
  pip3 install customtkinter
  ```
  
  ## Usage
  
  Here's how you can use Crunchy's Candy Wrapper:
  
  ```python
  import customtkinter as CTk
  from CrunchyCustomtkinterWrapper import *
  
  app = CustomTkinter()
  
  Main_Window(Title: "Whatever here", Size1: Integer, Size2: Integer)
                       ^^ window name        ^^ X axis        ^^ Y axis
  
  Main_Window_Scaled(Title: "Same thing", Size: Single Float
                              ^^ window name      ^^ Size as float like 800.64
  
  
  LightSwitch(Switch: bool)
    -  True is light mode
    -  False is dark mode
    -  None is system default
  
  Theme(color)
    -  "blue" sets to blue background (default in customtkinter)
    -  "green" sets to green background
    -  "dark-blue" or "darkblue" sets to darkblue background
  
  Custom_Theme(path)
                ^^ Put full path from root folder of project to your custom json theme
  
  now to the stuff people care about
  
  New_Button(button_text, Box_Text: string, Box_Row: int, Box_column: int, Box_paddx: int, Box_paddy: (range), callback: DefaultCallback
             ^^ Button text  ^^ Box text    ^ side X axis row  ^^  line row  ^^ Padx        ^ Padding  ^ (1 2) ^ existing Function name for logic

  New_(Box_identity, Box_Text: string, Box_Row: int, Box_column: int, Box_Padx: int, Box_Sticky: string normaly "w", Box_Sticky_custom: bool)
  to view what box    ^^ Box text      ^ box line row  ^ box up row    ^^ Padx        ^^ Box Sticky("anything")      ^ if true box_sticky_custom is valid
  

  
  app.mainloop()
  ```
  
  ## Dependencies
  
  The project has the following dependencies:
  
  - Customtkinter Latest (recommended)
  
  ## Contributing
  
  If you would like to contribute to this project, please follow these steps:
  
  1. Fork the repository
  2. Create a new branch (`git checkout -b feature`)
  3. Make your changes
  4. Commit your changes (`git commit -am 'Add new feature'`)
  5. Push to the branch (`git push origin feature`)
  6. Create a new Pull Request
  
  ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
