# This file intentionally left blank
import datetime
from tkfontchooser import askfont
import sys

# Has not been tested with Python2 since refactor.
# TODO: Test with Python2
if "2.7" in sys.version:
    import Tkinter
    from Tkinter import *
    from tkFileDialog import askopenfile, asksaveasfile
    from ScrolledText import *
    from tkColorChooser import askcolor
    import tkMessageBox as messagebox
    from ttk import Style
elif "3.6" in sys.version or "3.7" in sys.version:
    import tkinter
    from tkinter import *
    from tkinter.colorchooser import askcolor
    from tkinter.filedialog import askopenfile, asksaveasfile
    import tkinter.messagebox as messagebox
    import tkinter.scrolledtext
    from tkinter.ttk import Style

root = Tk(className="Just another Text Editor")
style = Style(root)
menu = Menu(root)
root.config(menu=menu)

# Determine python version
if "2.7" in sys.version:
    textPad = ScrolledText(root, width=100, height=80)
elif "3.6" in sys.version or "3.7" in sys.version:
    textPad = tkinter.scrolledtext.ScrolledText(root, width=100, height=80)
