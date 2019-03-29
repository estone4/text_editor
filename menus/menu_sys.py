import tkinter
from tkinter import Menu, Tk
from tkinter.ttk import Style
from functions import menu_functions
import startup

filemenu = Menu(startup.menu)
modifymenu = Menu(startup.root)
insertmenu = Menu(startup.root)
fontmenu = Menu(startup.root)
formatmenu = Menu(startup.menu)
personalizemenu = Menu(startup.root)
helpmenu = Menu(startup.menu)
# File menu
startup.menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=menu_functions.dummy_command)
filemenu.add_command(label="Open...", command=menu_functions.open_command)
filemenu.add_command(label="Save", command=menu_functions.save_command)
filemenu.add_separator()
# filemenu.add_cascade(label="Export", menu=exportmenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=menu_functions.exit_command)

# Modify menu
startup.menu.add_cascade(label="Modify",menu = modifymenu)
modifymenu.add_command(label="Copy", command = menu_functions.copy)
modifymenu.add_command(label="Paste", command=menu_functions.paste)
modifymenu.add_separator()
modifymenu.add_command(label = "Clear selection", command = menu_functions.clear)
modifymenu.add_command(label = "Clear all", command = menu_functions.clearall)

# Insert menu
startup.menu.add_cascade(label="Insert",menu= insertmenu)
insertmenu.add_command(label="Date",command=menu_functions.date)
insertmenu.add_command(label="Line",command=menu_functions.line)

# Font menu
startup.menu.add_cascade(label="Font", menu=fontmenu)
fontmenu.add_command(label="Choose font", command=menu_functions.font_chooser)

# Format menu
startup.menu.add_cascade(label="Format",menu = formatmenu)
formatmenu.add_command(label="Color...", command=menu_functions.font_color)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal',command=menu_functions.normal)
formatmenu.add_radiobutton(label='Bold',command=menu_functions.bold)
formatmenu.add_radiobutton(label='Underline',command=menu_functions.underline)
formatmenu.add_radiobutton(label='Italic',command=menu_functions.italic)

# Personalize menu
startup.menu.add_cascade(label="Personalize",menu=personalizemenu)
personalizemenu.add_command(label="Background...", command=menu_functions.background)

# Help menu
startup.menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=menu_functions.about_command)
# End of menu
