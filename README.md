# CTkPDFViewer
A simple yet powerfull pdf viewer for customtkinter! This can be helpful for adding documentation in the form of PDFs. Users can quicky view the offline copy of your documenation.

## Features
- load pdf with ease
- configure page width and height
- scrollable pages
- configurable options

## Installation
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/CTkPDFViewer?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/CTkPDFViewer/archive/refs/heads/main.zip)

**Requirements**
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) `pip install PyMuPDF`

**Download the source code, paste the `CTkPDFViewer` folder in the directory where your program is present.**

## Usage
```python
import customtkinter
from CTkPDFViewer import *

root = customtkinter.CTk()
root.geometry("700x600")
pdf_frame = CTkPDFViewer(root, file="my_file.pdf")
pdf_frame.pack(fill="both", expand=True, padx=10, pady=10)
root.mainloop()
```

## Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | parent widget  |
| **file** | the PDF file you want to view |
| page_width | **optional**, change the width of the pages |
| page_width | **optional**, change the height of the pages |
| page_separation_height | vhange the _pady_ between the pages |
| **other frame parameters | _All other ctkscrollable frame parameters can be passed_ |

You can change all these parameters using the `.configure()` method. Eg: `pdf_frame.configure(file="new_file.pdf", ...)`.

That's all, hope it can help!
