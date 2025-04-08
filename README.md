# CTkPDFViewer
A simple yet powerfull pdf viewer widget for customtkinter! This can be helpful for adding **documentation (in the form of PDF)** inside your application. 

Users can quicky view the offline copy of your documentation.

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
### CTkPDFViewer
```python
import customtkinter
from CTkPDFViewer import *

root = customtkinter.CTk()
root.geometry("700x600")
pdf_frame = CTkPDFViewer(root, file="my_file.pdf")
pdf_frame.pack(fill="both", expand=True, padx=10, pady=10)
root.mainloop()
```

![example](https://github.com/Akascape/CTkPDFViewer/assets/89206401/1324243e-da47-4bd8-af46-cded53cb7b51)

### CTkPDFViewerNavigate
```python
import customtkinter
from CTkPDFViewer import *

root = customtkinter.CTk()
root.geometry("700x600")
pdf_frame = CTkPDFViewerNavigate(root, file="my_file.pdf")
pdf_frame.pack(fill="both", expand=True, padx=10, pady=10)
root.mainloop()
```
![Snimak ekrana 2025-04-07 195103](https://github.com/user-attachments/assets/cb523b0a-0d6d-4d94-9340-a481fef3d0d8)

## Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | parent widget  |
| **file** | the PDF file you want to view |
| page_width | **optional**, change the width of the pages |
| page_height | **optional**, change the height of the pages |
| page_separation_height | change the _pady_ between the pages |
| **other frame parameters | _All other ctkscrollable frame parameters can be passed_ |

You can also change all these parameters using the `.configure()` method. Eg: `pdf_frame.configure(file="new_file.pdf", ...)`

That's all, hope it will help!
