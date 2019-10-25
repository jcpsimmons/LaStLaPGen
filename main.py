from constructors.htmlObj import HTMLObject
from constructors import htmlSnippets
from datetime import datetime
from bs4 import BeautifulSoup
import os


def fileHandling():
    PROJECT_NAME = input('\nWhat should I name the project directory? ')
    PROJECT_NAME = "{}-{}-{}_{}".format(str(datetime.now().year), str(datetime.now().month),
                                        str(datetime.now().day), PROJECT_NAME)
    os.system('mkdir ' + PROJECT_NAME)
    os.chdir(PROJECT_NAME)
    blank = input(
        '\nMade directory \"{}\". Move your image files into the folder and then press enter. Just press enter if there are no images to optimize.'.format(PROJECT_NAME))
    if len(os.listdir()) > 0:
        os.system("mkdir img")
        # optimize files
        os.system("jpegoptim -m90 *.jpg")
        os.system("jpegoptim -m90 *.jpeg")
        os.system("mv *.jpg img")
        os.system("mv *.jpeg img")
    else:
        print("\nI didn't find any images - continuing")
    return(PROJECT_NAME)


def locationParse(strLocation):
    # Turns raw string input (CSV) into array for location of object in 2D array
    insertLocation = strLocation.split(",")
    insertLocation = list(map(lambda x: int(x)-1, insertLocation))
    return(insertLocation)


def mappingSequence():
    # Creates HTMLObjects in a 2D array - each row has nested columns
    vdom = []
    hasVideo = False
    rows = int(input('\nHow many rows? '))
    for row in range(rows):
        colList = []
        cols = int(input('How many columns in row {}? '.format(str(row+1))))
        for col in range(cols):
            colList.append(HTMLObject(row + 1, col + 1))
        vdom.append(colList)

    # IMAGES
    numImages = int(input('\nHow many cells contain images (0 for none)? '))
    if numImages > 0:
        for i in range(numImages):
            insertLocation = input(
                '\nWhat is the location for image {} in row/col format, e.g. 1,3? '.format(str(i+1)))
            insertLocation = locationParse(insertLocation)
            altText = input('\nEnter alt text for this image: ')
            vdom[insertLocation[0]][insertLocation[1]].setImage(altText)

    # VIDEO
    isVideo = int(input('\nIs there a video (1 yes, 0 no)? '))
    if isVideo:
        insertLocation = input(
            '\nWhat is the location of the video in row/col format, e.g. 1,3? ')
        insertLocation = locationParse(insertLocation)
        altText = input('\nEnter alt text for the thumbnail image: ')
        link = input('\nEnter embed link for the YT video: ')
        vdom[insertLocation[0]][insertLocation[1]].setVideo(altText, link)

    # Assemble HTML
    finalHTML = ""
    for row in range(len(vdom)):
        columnCode = ""
        for col in range(len(vdom[row])):
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
    print("\nSaved file as {}.html".format(PROJECT_NAME))
except Exception as e:
    print(e)
