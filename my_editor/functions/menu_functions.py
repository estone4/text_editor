# Can be broken up into separate files based on menu entry.
from startup import initialize

def about_command():
    label = initialize.messagebox.showinfo("About", "Just Another TextPad \n Copyright \
    \n No rights left to reserve")

def dummy_command():
    print("I am a Dummy Command, I will be removed in the next step.")

def open_command():
    file = initialize.askopenfile(parent=initialize.root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        initialize.textPad.insert('1.0', contents)
        file.close()

def save_command():
    file = initialize.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = initialize.textPad.get('1.0', initialize.tkinter.END+'-1c')
        file.write(data)
        file.close()

def exit_command():
    if initialize.messagebox.askokcancel("Quit", "Do you really want to quit?"):
        initialize.root.destroy()

# Customization functions
def date():
    data = initialize.datetime.date.today()
    print(data)
    initialize.textPad.insert(initialize.tkinter.INSERT, data)

def line():
    lin = "_" * 60
    initialize.textPad.insert(initialize.tkinter.INSERT, lin)
#-------------------------------------------------------------------------------

# Font functions
def bold():
    initialize.textPad.config(font = ("Arial", 10, "bold"))

def font_chooser(): # Does not save changes to .txt file.
    font = initialize.askfont(initialize.root)
    if font:
        font['family'] = font['family'].replace(' ', '\ ')
    print(font)
    initialize.textPad.config(font = ("%(family)s %(size)i %(weight)s %(slant)s" % font))

def font_color():
    (triple,color) = initialize.askcolor()
    if color:
       initialize.textPad.config(foreground=color)

def italic():
    initialize.textPad.config(font = ("Arial",10,"italic"))

def normal():
    initialize.textPad.config(font = ("Arial", 10))

def underline():
    initialize.textPad.config(font = ("Arial", 10, "underline"))
#-------------------------------------------------------------------------------

# Editing functions
def copy():
    initialize.textPad.clipboard_clear()
    initialize.textPad.clipboard_append(initialize.textPad.selection_get())

def paste():
    try:
        teext = initialize.textPad.selection_get(selection='CLIPBOARD')
        initialize.textPad.insert(initialize.tkinter.INSERT, teext)
    except:
        initialize.messagebox.showerror("Error","The clipboard is empty!")

def clear():
    sel = initialize.textPad.get(initialize.tkinter.SEL_FIRST, initialize.tkinter.SEL_LAST)
    initialize.textPad.delete(initialize.tkinter.SEL_FIRST, initialize.tkinter.SEL_LAST)

def clearall():
    initialize.textPad.delete(1.0 , initialize.tkinter.END)
#-------------------------------------------------------------------------------

# Background functions
def background():
    (triple,color) = initialize.askcolor()
    if color:
       initialize.textPad.config(background=color)
#-------------------------------------------------------------------------------
