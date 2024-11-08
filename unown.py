import os
import string
from PIL import Image

# Function will create the images consisting of unowns
def stitch(imagePath):

    # resize the images
    images = [Image.open(path) for path in imagePath]

    #We want a line to store only 10 characters
    WIDTH = images[0].width * 10

    """
    To determine the height, we grab the amount of Lines
    then multiply by the image height.
    """
    n = len(images)  # grab number of characters
    
    #divide character by the 10 character limit per line to get line number.
    line = int(n / 10) if n % 10 == 0 else (int(n / 10) + 1)

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
    
# Function will convert user input to corresponding unowns
def convert(user, asciiToUnown):
    if not user:
        raise ValueError("Input Error: Empty String")

    user = user.upper()

    #Will use token at some point
    #token = list(user.split())
    sol = []
    for x in user:
        if x in asciiToUnown:
            sol.append(asciiToUnown[x])

    if not sol:
        raise ValueError("Input Error: No valid string")

    """
    Stitch the image then save and show user.
    """
    result = stitch(sol)
    return result

 #Function to create a dictionary of latin alphabet to unowns  
def initAsciiToUnown():
    folderName = "unown"
    #set the letter to the path of the unown 
    listOfUnown = []
    #create a list if alphabet and punctuation
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
        
        listOfUnown.append(os.path.join(folderName, fileName))

    #create hashtable of alphabet to unknown
    asciiToUnown = dict(zip(listOfAlphabet, listOfUnown))
    
    return asciiToUnown

def main():

    asciiToUnown = initAsciiToUnown()    
    try:
        user = input("What would you like to convert?:  ")
        result = convert(user, asciiToUnown)
        result.save('unown.png')
        result.show()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

