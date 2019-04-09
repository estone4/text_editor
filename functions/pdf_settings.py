import fpdf

from functions.menu_functions import font_chooser
import startup


def export_pdf():
    font = font_chooser()
    print(font)
    pdf = fpdf.FPDF()
    pdf.add_page()
    try:
        pdf.set_font(font['family'], size=font['size'])
    except RuntimeError:
        startup.messagebox.showerror(title="ERROR", message="Unsupported font.\nPlease select a different font.")
    pdf.multi_cell(190, 10, txt=startup.textPad.get('1.0', startup.tk.END+'-1c'))
    file = startup.asksaveasfile(mode='wb')
    if file is not None:
        pdf.output(name=file.name, dest='F').encode('latin-1')
    else:
        startup.messagebox.showerror(title="File Error", message="No file selected.")

