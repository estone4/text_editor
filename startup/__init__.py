import datetime
import sys

from tkfontchooser import askfont

print("Found Python version: {0}.{1}.{2}".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro))

if 2 == sys.version_info.major:
    import Tkinter as tk
    from Tkinter import Tk
    from tkFileDialog import askopenfile, asksaveasfile
    from ScrolledText import *
    from tkColorChooser import askcolor
    import tkMessageBox as messagebox
    from ttk import Style
elif 3 == sys.version_info.major:
    import tkinter as tk
    from tkinter import Tk
    from tkinter.colorchooser import askcolor
    from tkinter.filedialog import askopenfile, asksaveasfile
    import tkinter.messagebox as messagebox
    import tkinter.scrolledtext
    from tkinter.ttk import Style

root = Tk(className="Just another Text Editor")
style = Style(root)
menu = tk.Menu(root)
root.config(menu=menu)

# Determine python version
if 2 == sys.version_info.major:
    textPad = ScrolledText(root, width=100, height=80)
elif 3 == sys.version_info.major:
    textPad = tkinter.scrolledtext.ScrolledText(root, width=100, height=80)
