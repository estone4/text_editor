import sys

from functions import menu_functions
from functions import pdf_settings
import startup

if 2 == sys.version_info.major:
    from Tkinter import Menu
elif 3 == sys.version_info.major:
    from tkinter import Menu


file_menu = Menu(startup.menu)
modify_menu = Menu(startup.root)
insert_menu = Menu(startup.root)
font_menu = Menu(startup.root)
format_menu = Menu(startup.menu)
personalize_menu = Menu(startup.root)
help_menu = Menu(startup.menu)
export_menu = Menu(file_menu)

# File menu
startup.menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=menu_functions.dummy_command)
file_menu.add_command(label="Open...", command=menu_functions.open_command)
file_menu.add_command(label="Save", command=menu_functions.save_command)
file_menu.add_separator()
file_menu.add_cascade(label="Export", menu=export_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=menu_functions.exit_command)

# Modify menu
startup.menu.add_cascade(label="Modify", menu = modify_menu)
modify_menu.add_command(label="Copy", command = menu_functions.copy)
modify_menu.add_command(label="Paste", command=menu_functions.paste)
modify_menu.add_separator()
modify_menu.add_command(label="Clear selection", command = menu_functions.clear)
modify_menu.add_command(label="Clear all", command = menu_functions.clear_all)

# Insert menu
startup.menu.add_cascade(label="Insert", menu= insert_menu)
insert_menu.add_command(label="Date", command=menu_functions.date)
insert_menu.add_command(label="Line", command=menu_functions.line)

# Font menu
startup.menu.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Choose font", command=menu_functions.font_chooser)

# Format menu
startup.menu.add_cascade(label="Format", menu = format_menu)
format_menu.add_command(label="Color...", command=menu_functions.font_color)
format_menu.add_separator()
format_menu.add_radiobutton(label='Normal', command=menu_functions.normal)
format_menu.add_radiobutton(label='Bold', command=menu_functions.bold)
format_menu.add_radiobutton(label='Underline', command=menu_functions.underline)
format_menu.add_radiobutton(label='Italic', command=menu_functions.italic)

# Personalize menu
startup.menu.add_cascade(label="Personalize", menu=personalize_menu)
personalize_menu.add_command(label="Background...", command=menu_functions.background)

# Help menu
startup.menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About...", command=menu_functions.about_command)

# Export submenu
export_menu.add_command(label="PDF", command=pdf_settings.export_pdf)
# End of menu
