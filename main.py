from PIL import Image, ImageDraw, ImageFont
import os
from tkinter import Tk, Entry, Button, Label, filedialog, END


def tagImages():
    try:
        # Start by getting a list of files in given folder
        imageList = os.listdir(sourcePath)

        # List tge allowable image endings
        imgEndings = ["jpg", "jepg", "png", "gif"]

        # Loop over filenames in temporary list
        tmpList = imageList.copy()
        for x in tmpList:
            # Remove filenames not matching image endings
            if (x[-4:] not in imgEndings) and (x[-3:] not in imgEndings):
                imageList.remove(x)

        if len(imageList) == 0:
            print("No images present in selected folder")
            outputLabel.config(text = "No images present in selected folder")
            return
            

        # Loop over all images
        for x in imageList: 
            # Open image
            image = Image.open("Test/" + x)
            # Call draw Method to add 2D graphics in an image
            I1 = ImageDraw.Draw(image) 

            # Calculate text coordinate location
            textCoord = (int(25), int(image.size[1]*19/20))

            # Font setup, size is 80
            myFont = ImageFont.truetype('Fonts/DejaVuSans.ttf', 80)

            # Wrtie text onto image
            I1.text(textCoord, x, font = myFont, fill=(0, 255, 0))

            # Save image
            image.save(destPath + "/" + x)

        print("Image generation successful, %d pictures tagged." %len(imageList))
        outputLabel.config(text = "Image generation successful, %d pictures tagged." %len(imageList))

    except:
        print("An error has occured.")
        outputLabel.config(text = "An error has occured.")
    
def select_source_file():
    global sourcePath
    sourcePath = filedialog.askdirectory(title="Select a File")
    e1.delete(0, END)
    e1.insert(0, sourcePath)

def select_dest_file():
    global destPath
    destPath = filedialog.askdirectory(title="Select a File")
    e2.delete(0, END)
    e2.insert(0, destPath)
    

m = Tk()
m.title('Image Tag 4000')
sourcePath = ""
destPath = ""

e1 = Entry(m, width=100)
e2 = Entry(m, width=100)
e1.grid(row=0, columnspan=2)
e2.grid(row=1, columnspan=2)

outputLabel = Label(m, text='Select files for generation',  width=50)
outputLabel.grid(row = 2, columnspan = 2)

button1 = Button(m, text='Tag', width=50, command=tagImages)
button2 = Button(m, text='Exit', width=50, command=m.destroy)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)

buttonSelectSource = Button(m, text='Select source', width=20, command=select_source_file)
buttonSelectDest = Button(m, text='Select Destination', width=20, command=select_dest_file)
buttonSelectSource.grid(row=0, column=3)
buttonSelectDest.grid(row=1, column=3)

m.mainloop()
