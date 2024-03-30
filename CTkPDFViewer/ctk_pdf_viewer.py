"""
CTkPDFViewer is a pdf viewer widget for customtkinter.
Author: Akash Bora
License: MIT
"""

import customtkinter
from PIL import Image
import fitz
from threading import Thread
import math
import io
import os

class CTkPDFViewer(customtkinter.CTkScrollableFrame):

    def __init__(self,
                 master: any,
                 file: str,
                 page_width: int = 600,
                 page_height: int = 700,
                 page_separation_height: int = 2,
                 **kwargs):
        
        super().__init__(master, **kwargs)

        self.page_width = page_width
        self.page_height = page_height
        self.separation = page_separation_height
        self.pdf_images = []
        self.labels = []
        self.file = file

        self.percentage_view = 0
        self.percentage_load = customtkinter.StringVar()
        
        self.loading_message = customtkinter.CTkLabel(self, textvariable=self.percentage_load, justify="center")
        self.loading_message.pack(pady=10)

        self.loading_bar = customtkinter.CTkProgressBar(self, width=100)
        self.loading_bar.set(0)
        self.loading_bar.pack(side="top", fill="x", padx=10)

        self.after(250, self.start_process)

    def start_process(self):
        Thread(target=self.add_pages).start()
        
    def add_pages(self):
        """ add images and labels """
        self.percentage_bar = 0
        open_pdf = fitz.open(self.file)
        
        for page in open_pdf:
            page_data = page.get_pixmap()
            pix = fitz.Pixmap(page_data, 0) if page_data.alpha else page_data
            img = Image.open(io.BytesIO(pix.tobytes('ppm')))
            label_img = customtkinter.CTkImage(img, size=(self.page_width, self.page_height))
            self.pdf_images.append(label_img)
                
            self.percentage_bar = self.percentage_bar + 1
            percentage_view = (float(self.percentage_bar) / float(len(open_pdf)) * float(100))
            self.loading_bar.set(percentage_view)
            self.percentage_load.set(f"Loading {os.path.basename(self.file)} \n{int(math.floor(percentage_view))}%")
            
        self.loading_bar.pack_forget()
        self.loading_message.pack_forget()
        open_pdf.close()
        
        for i in self.pdf_images:
            label = customtkinter.CTkLabel(self, image=i, text="")
            label.pack(pady=(0, self.separation))
            self.labels.append(label)
        
    def configure(self, **kwargs):
        """ configurable options """
        
        if "file" in kwargs:
            self.file = kwargs.pop("file")
            self.pdf_images = []
            for i in self.labels:
                i.destroy()
            self.labels = []
            self.after(250, self.start_process)
            
        if "page_width" in kwargs:
            self.page_width = kwargs.pop("page_width")
            for i in self.pdf_images:
                i.configure(size=(self.page_width, self.page_height))
                
        if "page_height" in kwargs:
            self.page_height = kwargs.pop("page_height")
            for i in self.pdf_images:
                i.configure(size=(self.page_width, self.page_height))
            
        if "page_separation_height" in kwargs:
            self.separation = kwargs.pop("page_separation_height")
            for i in self.labels:
                i.pack_forget()
                i.pack(pady=(0,self.separation))
        
        super().configure(**kwargs)
