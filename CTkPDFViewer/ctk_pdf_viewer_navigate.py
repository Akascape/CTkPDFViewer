"""
CTkPDFViewer is a pdf viewer widget for customtkinter.
Author: Akash Bora
License: MIT
"""

import customtkinter
from PIL import Image
import fitz
import io


class CTkPDFViewerNavigate(customtkinter.CTkFrame):

    def __init__(self,
                 master: any,
                 file: str,
                 page_width: int = 600,
                 page_height: int = 700,
                 **kwargs):
        
        super().__init__(master, **kwargs)

        self.page_width = page_width
        self.page_height = page_height
        self.file = file

        self.current_page = 0
        self.total_pages = 0
        self.open_pdf = None
        self.page_images = []

        # Create widgets
        self.image_label = customtkinter.CTkLabel(self, text="")
        self.image_label.pack(pady=10)

        self.navigation_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.navigation_frame.pack(pady=10)

        self.left_button = customtkinter.CTkButton(self.navigation_frame, text="◀", command=self.prev_page)
        self.left_button.pack(side="left", padx=10)

        self.page_entry = customtkinter.CTkEntry(self.navigation_frame, width=50, validate="key", justify="right",
                                                 border_width=0, fg_color="transparent")
        self.page_entry.pack(side="left", padx=1)
        self.page_entry.configure(validatecommand=(self.register(self.validate_number), "%P"))
        self.page_entry.bind("<Return>", self.goto_page)
        self.page_entry.bind("<KeyRelease>", self.goto_page_key_release)

        self.total_pages_label = customtkinter.CTkLabel(self.navigation_frame, text="")
        self.total_pages_label.pack(side="left", padx=(0, 10))

        self.right_button = customtkinter.CTkButton(self.navigation_frame, text="▶", command=self.next_page)
        self.right_button.pack(side="left", padx=10)

        self.load_pdf()

    def load_pdf(self):
        """ Load the PDF file and extract page images """
        self.open_pdf = fitz.open(self.file)
        self.total_pages = len(self.open_pdf)

        self.page_images = []
        for page in self.open_pdf:
            pixmap = page.get_pixmap()
            pix = fitz.Pixmap(pixmap, 0) if pixmap.alpha else pixmap
            img = Image.open(io.BytesIO(pix.tobytes("ppm")))
            resized_img = img.resize((self.page_width, self.page_height))
            ctk_image = customtkinter.CTkImage(resized_img, size=(self.page_width, self.page_height))
            self.page_images.append(ctk_image)

        self.total_pages_label.configure(text=f"/{self.total_pages}")
        self.show_page(0)

    def validate_number(self, value: str) -> bool:
        """ Validate that the input contains only numbers """
        return value.isdigit() or value == ""

    def show_page(self, page_number: int):
        """ Display the specified page number """
        if 0 <= page_number < self.total_pages:
            self.current_page = page_number
            self.image_label.configure(image=self.page_images[page_number])

            self.page_entry.delete(0, "end")
            self.page_entry.insert(0, str(self.current_page + 1))

    def prev_page(self):
        """ Navigate to the previous page """
        if self.current_page > 0:
            self.show_page(self.current_page - 1)

    def next_page(self):
        """ Navigate to the next page """
        if self.current_page < self.total_pages - 1:
            self.show_page(self.current_page + 1)

    def goto_page(self, event=None):
        """ Navigate to a specific page entered by the user """
        try:
            page_number = int(self.page_entry.get()) - 1
            if 0 <= page_number < self.total_pages:
                self.show_page(page_number)
        except ValueError:
            pass  # Ignore invalid input

    def goto_page_key_release(self, event=None):
        """ Navigate to the page during key release """
        try:
            page_number = int(self.page_entry.get()) - 1
            if 0 <= page_number < self.total_pages:
                self.show_page(page_number)
        except ValueError:
            pass  # Ignore invalid input
