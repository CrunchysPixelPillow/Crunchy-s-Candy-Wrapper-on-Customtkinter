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

1. Clone the repository:

```bash
git clone https://github.com/username/Crunchy-s-Candy-Wrapper-on-Customtkinter.git
```

2. Install Customtkinter:

```bash
pip install customtkinter
```

## Usage

Here's how you can use Crunchy's Candy Wrapper:

```python
import customtkinter as CTk
from CrunchyCustomtkinterWrapper import *

Main_Window(Title: "Whatever here", Size1: Integer, Size2: Integer)
                     ^^ window name        ^^ X axis        ^^ Y axis
app = CustomTkinter()
app.create_window("Crunchy's Candy Wrapper", 400, 300)
app.add_label("Custom Candy Wrapper")
app.add_button("Generate Wrapper", generate_wrapper)
app.run()
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
