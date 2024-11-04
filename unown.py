import os
import string
from PIL import Image


def resize(imagePath, fontSize):
    with Image.open(imagePath) as img:
        dpi = 130
        height = int((fontSize/72) * dpi)
        newSize = (int(img.width * (height / img.height)), height)
        return img.resize(newSize)


def stitch(imagePath):

    # resize the images
    images = [resize(path, 32) for path in imagePath]

    #We want a line to store only 10 characters
    WIDTH = images[0].width * 10

    """
    To determine the height, we grab the amount of Lines
    then multiply by the image height.
    """
    n = len(images)  # grab number of characters
    line = 0
    #divide character by the 10 character limit per line to get line number.
    if n % 10 == 0: 
        line = n / 10
    else:
        line = n//10 + 1

    HEIGHT = line * images[0].height

    #Create a new image
    stitchedImage = Image.new('RGBA', (WIDTH, HEIGHT))

    # keeps track of the current image location
    xOffset = 0
    yOffset = 0
    
    for img in images:
        """
        if the image width with its offset is greater 
        than the resulting image width
        we push it onto the next line of the page
        """
        if xOffset + img.width > WIDTH:
            xOffset = 0
            #increase the y offset
            yOffset += img.height

        #copy image onto the resulting image
        stitchedImage.paste(img,(xOffset, yOffset))
        #increment the x offset by the image width
        xOffset += img.width

    return stitchedImage
    

def main():
    file = "unown"

    #set the letter to the path of the unown
    listOfUnown = []
    listOfAlphabet = list(string.ascii_uppercase) + ['!', '?', ' ', '-']

    for val in listOfAlphabet:
        fileName = ""

        if val == '?':
            fileName = "question.png"
        elif val == ' ':
            fileName = "blank.png"
        elif val == '-':
            fileName = "-.png"
        else:
            fileName = val + ".png"
        
        listOfUnown.append(os.path.join(file, fileName))

    asciiToUnown = dict(zip(listOfAlphabet, listOfUnown))

    user = input("What would you like to convert?:  ")
    user = user.upper()

    #Will use token at some point
    #token = list(user.split())
    sol = []
    for x in user:
        if x in asciiToUnown:
            sol.append(asciiToUnown[x])

    result = stitch(sol)
    result.save('unown.png')
    result.show()


if __name__ == "__main__":
    main()

