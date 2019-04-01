import fpdf

from functions.menu_functions import font_chooser
import startup

def export_pdf():
    font = font_chooser()
    print(font)
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font(font['family'], size=font['size'])
    pdf.multi_cell(190, 10, txt=startup.textPad.get('1.0', startup.tkinter.END+'-1c'))
    file = startup.asksaveasfile(mode='wb')
    pdf.output(name=file.name, dest='F').encode('latin-1')
