from fpdf import FPDF
import menus.menu_sys
import startup

# Determine OS
if "win" == startup.sys.platform[:3]:
    startup.style.theme_use('vista')
elif "darwin" in startup.sys.platform:
    startup.style.theme_use('clam')
else:
    startup.style.theme_use('clam')

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
