from PIL import Image, ImageDraw, ImageFont
import os

# First, start by getting a list of files in given folder
imageList = os.listdir("Test")

# List tge allowable image endings
imgEndings = ["jpg", "jepg", "png", "gif"]

# Loop over filenames in temporary list
tmpList = imageList.copy()
for x in tmpList:
    # Remove filenames not matching image endings
    if (x[-4:] not in imgEndings) and (x[-3:] not in imgEndings):
        imageList.remove(x)
    

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
    image.save("Tagged/" + x)
    
    
    
