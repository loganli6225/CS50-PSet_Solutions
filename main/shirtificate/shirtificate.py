from fpdf import FPDF
from fpdf import Align

class PDF(FPDF): # Option 1
    def header(self):
        self.set_font("helvetica", "B", 60)
        self.cell(None, 50, "CS50 Shirtificate", center = True)

name = input("Name: ")
pdf = PDF() # Option 1
# pdf = FPDF() # Option 2
pdf.add_page()
pdf.set_auto_page_break(auto = False)

# Creates Header # Option 2
# pdf.set_font("helvetica", "B", 60)
# pdf.cell(None, 50, "CS50 Shirtificate", center = True)

# Creates Image
pdf.image("shirtificate.png", x = Align.C, y = 75, h = 180)

# Creates Shirt Text
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.cell(None, 225, f"{name} took CS50", center = True)

pdf.output("shirtificate.pdf")
