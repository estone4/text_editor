import fpdf
from functions.menu_functions import font_chooser
import startup
# TODO: wrap text in pdf
# TODO: allow user to specify file name
def export_pdf():
    font = font_chooser()
    print(font)
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font(font['family'], size=font['size'])
    pdf.cell(200, 10, txt=startup.textPad.get('1.0', startup.tkinter.END+'-1c'))
    #file = startup.asksaveasfile(mode='wb')
    pdf.output(name='My_Export.pdf', dest='F').encode('latin-1')