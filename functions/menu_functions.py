# Can be broken up into separate files based on menu entry.
import startup


def about_command():
    startup.messagebox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")


def dummy_command():
    print("I am a Dummy Command, I will be removed in the next step.")


def open_command():
    file = startup.askopenfile(parent=startup.root, mode='rb', title='Select a file')
    if file is not None:
        contents = file.read()
        startup.textPad.insert('1.0', contents)
        file.close()


def save_command():
    file = startup.asksaveasfile(mode='w')
    if file is not None:
        # slice off the last character from get, as an extra return is added
        data = startup.textPad.get('1.0', startup.tkinter.END+'-1c')
        file.write(data)
        file.close()


def exit_command():
    if startup.messagebox.askokcancel(title="Quit", message="Do you really want to quit?"):
        startup.root.destroy()


# Customization functions
def date():
    data = startup.datetime.date.today()
    print(data)
    startup.textPad.insert(startup.tkinter.INSERT, data)


def line():
    lin = "_" * 60
    startup.textPad.insert(startup.tkinter.INSERT, lin)
# -------------------------------------------------------------------------------


# Font functions
def bold():
    startup.textPad.config(font=("Arial", 10, "bold"))


def font_chooser():  # Does not save changes to .txt file.
    font = startup.askfont(startup.root)
    if font:
        # noinspection PyPep8
        font['family'] = font['family'].replace(' ', '\ ')
    print(font)
    startup.textPad.config(font=("%(family)s %(size)i %(weight)s %(slant)s" % font))
    return font


def font_color():
    (triple, color) = startup.askcolor()
    if color:
        startup.textPad.config(foreground=color)


def italic():
    startup.textPad.config(font=("Arial", 10, "italic"))


def normal():
    startup.textPad.config(font=("Arial", 10))


def underline():
    startup.textPad.config(font=("Arial", 10, "underline"))
# -------------------------------------------------------------------------------


# Editing functions
def copy():
    startup.textPad.clipboard_clear()
    startup.textPad.clipboard_append(startup.textPad.selection_get())


def paste():
    try:
        teext = startup.textPad.selection_get(selection='CLIPBOARD')
        startup.textPad.insert(startup.tkinter.INSERT, teext)
    except Exception as e:
        startup.messagebox.showerror(title="Error", message="The clipboard is empty!\n" + str(e))


def clear():
    startup.textPad.delete(startup.tkinter.SEL_FIRST, startup.tkinter.SEL_LAST)


def clear_all():
    startup.textPad.delete(1.0, startup.tkinter.END)
# -------------------------------------------------------------------------------


# Background functions
def background():
    (triple, color) = startup.askcolor()
    if color:
        startup.textPad.config(background=color)
# -------------------------------------------------------------------------------
