from fpdf import FPDF
import menus.menu_sys
import startup.initialize as startup

# Determine OS
if "win" == startup.sys.platform[:3]:
    startup.style.theme_use('vista')
elif "darwin" in startup.sys.platform:
    startup.style.theme_use('clam')
else:
    startup.style.theme_use('clam')

# # Determine python version
# if "2.7" in startup.initialize.sys.version:
#     textPad = ScrolledText(root, width=100, height=80)
# elif "3.6" in startup.initialize.sys.version or "3.7" in startup.initialize.sys.version:
#     textPad = startup.initialize.tkinter.scrolledtext.ScrolledText(startup.initialize.root, width=100, height=80)

bg = startup.style.lookup("TLabel", "background")
startup.root.configure(bg=bg)

# TODO: implement export to pdf functionality
def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(font['family'], size=font['size'])
    pdf.cell(200, 10, text=textPad.get('1.0', END+'-1c'))
    pdf.output(asksaveasfile(mode='w'))
#-------------------------------------------------------------------------------

startup.root.config(menu=startup.menu)

startup.textPad.pack()

startup.root.mainloop()
