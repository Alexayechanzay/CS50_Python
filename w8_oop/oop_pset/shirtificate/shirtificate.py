from fpdf import FPDF, Align

pdf = FPDF(orientation="P", unit="mm", format="A4")

# name input
name = input("Name: ").strip()

pdf.add_page()
pdf.set_font("helvetica", style="B", size=50)
pdf.cell(text="CS50 Shirtificate", center=True)

# adding image to the page 
pdf.set_y(50)
pdf.image(name="shirtificate.png", x=Align.C, w=180, h=220)

# Finding the center 
pg_width = pdf.w
pg_height = pdf.h
row_height = 10
center_y = (pg_height /2) - (row_height /2)

# moving the cursor to the centered position
pdf.set_y(center_y)

# write a name text
pdf.set_font("helvetica", size=26)
pdf.set_text_color("#FFFFFF")
pdf.multi_cell(w=0, h=row_height, text=f"{name} took CS50", align="C")

# output 
pdf.output(f"shirtificate.pdf")