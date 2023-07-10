from fpdf import FPDF

def main():

    user_input = input("Name: ")

    pdf = FPDF()

    pdf.orientation = 'portrait'
    pdf.format = 'A4'
    pdf.add_page()
    pdf.image('shirtificate.png', 'C')

    pdf.set_text_color(255,255,255)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, -300, txt=user_input, ln=1, align="C")
    pdf.output("shirtificate.pdf")





if __name__ == '__main__':
    main()
