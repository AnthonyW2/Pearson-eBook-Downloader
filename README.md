# Pearson eBook Downloader

This tool downloads the pages of any Pearson eBook as they are stored on Pearson's servers - as individual PNGs.

It is meant to make it easier for people with slow internet, or who dislike Pearson's reader application.

You may do what you like with this tool - copy the code, use it any way you like, but **I will not be held accountable for how it is used**.
**Piracy is a crime, and I do not endorse it in any form. You are entirely responsible for your own actions.**

<br>

## Python Script

Brief steps for using the python-based tool:
1. Clone this repository to your local computer.
2. Ensure you have the "requests" python library installed.
3. Get the URL of the pages. [Detailed instructions](###Getting-the-URL-of-the-book-pages) on how to do that are below.
4. Run `download.py` in python, supplying the URL of the pages as a command-line argument:<br>
   `python download.py <Your URL goes here>`
   You can also supply the start and end page numbers as arguments after the URL.
5. To concatenate the downloaded images into a single PDF, you can either use the supplied python script, or use another program such as LibreOffice. [Detailed instructions](###Converting-to-a-PDF) on how to do that are below.
6. Optionally, you may use an OCR tool such as [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) to add a text layer to the PDF. This is necessary to be able to select and copy the text in the book, because downloading the pages from Pearson only yields images which have no text data attached to them.

<br>

### Getting the URL of the book pages

To obtain the URL of the pages which you need to supply to the tool:
1. Go to [Pearson Places](https://www.pearsonplaces.com.au/dash) and log in.
2. Open your target eBook. (Some ad-blockers or other extensions may prevent the book from opening, so if you have trouble try disabling your browser extensions).
3. Press Ctrl+Shift+C to open the developer tools and inspect the page. Alternatively (if that doesn't work), press Ctrl+Shift+I, then in the top-left of the developer tools select "Pick an element from the page".
4. Hover over and click on the page in the eBook viewer (this should be the front cover of the book, displayed in the right-hand half of the window)
5. In the developer tools, an <img\> element with a large URL should be selected.
6. Right-click on this URL and select "Copy link address".
7. The link you just copied should have the form `https://______________.cloudfront.net/resources/products/epubs/generated/________-____-____-____-____________/foxit-assets/pages/page0`, with some stuff on the end of it.
8. You should now be able to use that link for the tool.

<br>

### Converting to a PDF
Once you have downloaded all pages of your eBook, you will be left with hundreds of PNG images.
The following steps outline the process to concatenate them into a single PDF using either the supplied python script or LibreOffice.

#### Python Script:

To concatenate the images into a PDF using the python script in this repository:
1. Take note of the filepath to the directory containing all downloaded images.
2. Run `pages2pdf.py` in python, supplying the filepath to the directory with the images as a command-line argument:<br>
   `python pages2pdf.py /path/to/directory/with/images`
   You can also supply the output file name as another argument after the filepath.

#### LibreOffice:

To add the images to a PDF in LibreOffice:
1. Open LibreOffice, and create a new "Impress" presentation. You can press cancel to any extra dialogue on startup.
2. In the "Properties" panel (on the right-hand side of the screen by default), make sure the "Format" (or aspect ratio) and Orientation are correct.
3. When inserted, the images will not change the shape of the slide, so make sure to set the aspect ratio to match the images.
4. Go to Insert > Media > Photo Album
5. Select "Add" in the popup window.
6. Navigate to the folder/directory containing the downloaded images, and select all of them.
7. Once you have selected/highlighted all the pages/images, select "Open".
8. Now that you have added the images as an album, select "Insert Slides" in the popup window. This may take a very long time, depending on the speed of your computer. I'd recommend using Task Manager in Windows, or any process manager/resource monitor of your choice (such as Htop in Linux) to monitor LibreOffice.
9. Once the process has completed, delete the first slide (which would have been created with the new presentation, and will not have an image on it). This can be achieved by simply right-clicking on it in the left panel and selecting "Delete".
10. Feel free to remove or edit other pages/slides as you see fit.
11. Finally, to export the presentation as a PDF, go to "File" > "Export As" > "Export Directly As PDF"
12. Rename it to your desired name, choose a suitable save location, and select "Save".
13. You can now close LibreOffice without saving, as you now have the presentation in PDF form.

<br>

## Browser version

Note: **The browser version of this tool is now deprecated**, since it wasn't very user-friendly, and download confirmation-prompts break it.

Brief steps for using the browser-based tool:
1. Clone this repository to your local computer.
2. Open the main index.html file in your web browser of choice.
3. Follow the instructions at the bottom of the page on how to use it.
