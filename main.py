from constructors.htmlObj import HTMLObject
from constructors import htmlSnippets
from functions.printFunctions import inputClear
from functions.misc import locationParse

from datetime import datetime
from bs4 import BeautifulSoup
import os
import time


def fileHandling():
    PROJECT_NAME = inputClear('What should I name the project directory? ')
    PROJECT_NAME = "{}-{}-{}_{}".format(str(datetime.now().year), str(datetime.now().month),
                                        str(datetime.now().day), PROJECT_NAME)
    os.system('mkdir ' + PROJECT_NAME)
    os.chdir(PROJECT_NAME)
    blank = inputClear(
        'Made directory \"{}\". Move your image files into the folder created on your and then press enter. Just press enter if there are no images to optimize.'.format(PROJECT_NAME))
    if len(os.listdir()) > 0:
        os.system("mkdir img")
        # optimize files
        os.system("jpegoptim -m90 *.jpg")
        os.system("jpegoptim -m90 *.jpeg")
        os.system("mv *.jpg img")
        os.system("mv *.jpeg img")
    else:
        print("I didn't find any images - continuing")
        time.sleep(1)
    return(PROJECT_NAME)


def mappingSequence():
    # Creates HTMLObjects in a 2D array - each row has nested columns
    vdom = []
    hasVideo = False
    rows = int(inputClear('How many rows? '))
    for row in range(rows):
        colList = []
        cols = int(inputClear('How many columns in row {}? '.format(str(row+1))))
        for col in range(cols):
            colList.append(HTMLObject(row + 1, col + 1))
        vdom.append(colList)

    # IMAGES
    numImages = int(inputClear('How many cells contain images (0 for none)? '))
    if numImages > 0:
        for i in range(numImages):
            insertLocation = inputClear(
                'What is the location for image {} in row/col format, e.g. 1,3? '.format(str(i+1)))
            insertLocation = locationParse(insertLocation)
            altText = inputClear('Enter alt text for this image: ')
            vdom[insertLocation[0]][insertLocation[1]].setImage(altText)

    # VIDEO
    isVideo = int(inputClear('Is there a video (1 yes, 0 no)? '))
    if isVideo:
        hasVideo = True
        insertLocation = inputClear(
            'What is the location of the video in row/col format, e.g. 1,3? ')
        insertLocation = locationParse(insertLocation)
        altText = inputClear('Enter alt text for the thumbnail image: ')
        link = inputClear('Enter embed link for the YT video: ')
        vdom[insertLocation[0]][insertLocation[1]].setVideo(altText, link)

    # Assemble HTML
    finalHTML = ""
    for row in range(len(vdom)):
        columnCode = ""
        for col in range(len(vdom[row])):
            flexBasis = inputClear(
                'Set flex basis percentage for row {} column {}. (Enter for 50% default): '.format(str(row+1), str(col + 1)))
            vdom[row][col].setFlexBasis(flexBasis)
            columnCode = columnCode + \
                vdom[row][col].renderComponent()
        rowCode = "<div class='container {}'>{}</div>".format(
            "row{}".format(str(row+1)), columnCode)
        finalHTML = finalHTML + rowCode

    if hasVideo:
        finalHTML = finalHTML + htmlSnippets.videoModal
        finalHTML = htmlSnippets.cssWithVideoModal + \
            "<div class='x'>" + finalHTML + "</div>"
    else:
        finalHTML = htmlSnippets.css + "<div class='x'>" + finalHTML + "</div>"
    return(finalHTML)


PROJECT_NAME = fileHandling()
vdom = mappingSequence()
# prettify the HTML
vdom = BeautifulSoup(vdom, "html.parser")
vdom = vdom.prettify()

filename = PROJECT_NAME + '.html'

try:
    with open(filename, 'w') as file:
        file.write(vdom)
    print("Saved file as {}.html".format(PROJECT_NAME))
except Exception as e:
    print(e)
