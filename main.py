from PIL import Image, ImageDraw, ImageFont
import os
from tkinter import Tk, ttk, Entry, Button, Label, filedialog, END, StringVar


def tagImages():
    try:
        # Start by getting a list of files in given folder
        imageList = os.listdir(sourcePath)

        # List tge allowable image endings
        imgEndings = ["jpg", "jepg"]

        # Loop over filenames in temporary list
        tmpList = imageList.copy()
        for x in tmpList:
            # Remove filenames not matching image endings
            if (x[-4:] not in imgEndings) and (x[-3:] not in imgEndings):
                imageList.remove(x)

        if len(imageList) == 0:
            print("No images present in selected folder")
            label_text.set("No images present in selected folder")
            return
            
        imageCount = 0
        # Loop over all images
        for x in imageList:
            imageCount += 1
            print(x)
            label_text.set("Tagging picture %d of %d..." %(imageCount, len(imageList)))
            m.update()
            # Open image
            image = Image.open(sourcePath + "/" + x)
            # Call draw Method to add 2D graphics in an image
            I1 = ImageDraw.Draw(image) 

            # Calculate text coordinate location
            textCoord = (int(25), int(25))

            # Font setup, size is 80
            myFont = ImageFont.truetype('Fonts/DejaVuSans.ttf', 80)

            # Wrtie text onto image
            I1.text(textCoord, x, font = myFont, fill=(0, 255, 0))

            # Save image
            image.save(destPath + "/" + x)

        print("Image generation successful, %d pictures tagged." %len(imageList))
        label_text.set("Image generation successful, %d pictures tagged." %len(imageList))

    except:
        print("An error has occured.")
        label_text.set("An error has occured.")
    
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

label_text = StringVar()
label_text.set('Select files for generation')
outputLabel = Label(m, textvariabl=label_text,  width=50)
outputLabel.grid(row = 2, columnspan = 2)

button1 = Button(m, text='Tag', width=50, command=tagImages)
button2 = Button(m, text='Exit', width=50, command=m.destroy)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)

buttonSelectSource = Button(m, text='Select source', width=20, command=select_source_file)
buttonSelectDest = Button(m, text='Select Destination', width=20, command=select_dest_file)
buttonSelectSource.grid(row=0, column=3)
buttonSelectDest.grid(row=1, column=3)

#pb = ttk.Progressbar(
#    m,
#    orient='horizontal',
#    mode='indeterminate',
#    length=500
#)

#pb.grid(row = 4, column = 0, columnspan = 2)

m.mainloop()
