from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, text):
        super().__init__("P", "mm", "A4")
        self.add_page()
        self.page_width = self.w
        self.page_height = self.h
        self.text = text

    # add title text to page
    def add_title(self):
        self.set_font("helvetica", size=50)
        x_txt = (self.page_width - self.get_string_width("CS50 Shirtificate")) / 2
        self.set_x(x_txt)
        self.cell(None, 30, "CS50 Shirtificate", align="C")

    # add image to page
    def add_image(self):
        image_width = 180
        image_height = 200
        x_img = (self.page_width - image_width) / 2
        y_img = (self.page_height - image_height) / 1.5
        self.image("shirtificate.png", x=x_img, y=y_img, w=image_width, h=image_height)

        # add text to image
        self.set_xy(self.page_width/25, self.page_height/2)
        self.set_font("helvetica", size=25)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{self.text} took CS50", align="C")

    # get shirtificate
    def get_shirtificate(self):
        self.add_title()
        self.add_image()


def main():
    # get user's input
    name = input("Name: ").strip().title()

    # create instance of Shirtificate class
    pdf = Shirtificate(name)
    pdf.get_shirtificate()

    # display file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
